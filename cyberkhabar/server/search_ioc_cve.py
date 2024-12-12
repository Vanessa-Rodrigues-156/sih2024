import requests
import json
import time
from itertools import cycle
import re

# OTX and VirusTotal API Keys
otx_api_keys = [
    "848a57e9cb738116d0080f0c0781dbc7fec74c5bc95f9d24b6ca633888d187f8",
    "3fb1b0d7e576ac2ab2e092b658f9262f7ab36469b9223732c1f0f30c82be8d59",
    "f21a04f9f2be5c6ea689df2c65018f035b1861c5d4f726190eac676a33e2b5a7"
]

vt_api_keys = [
    "0469f7a868fbd190df6474007b0bb311e80614f14d4a825f8f78f8351a7b2eed",
    "a3c09e19c3359dc4584c99a2cb90bfb2a67adce4db58fda37b294df288ac3f80",
    "4ac2dbf4ddc43894cfb5a15e25b5c5d97ce1fa1b3aafb2f414c32edec9ac8dbd"
]

# Cycle through API keys to avoid rate limits
otx_api_key_cycle = cycle(otx_api_keys)
vt_api_key_cycle = cycle(vt_api_keys)

# Step 1: Search IOC in OTX
def search_otx(ioc_value, ioc_type):
    """
    Search for an IOC in OTX and return the results.
    """
    api_key = next(otx_api_key_cycle)
    headers = {"X-OTX-API-KEY": api_key}
    url = f"https://otx.alienvault.com/api/v1/indicators/{ioc_type}/{ioc_value}"

    print(f"Searching OTX for {ioc_type.upper()}: {ioc_value}...")
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 404:
        print("No results found in OTX.")
        return {}
    else:
        print(f"Error {response.status_code} from OTX.")
        return {}

# Step 2: Search IOC in VirusTotal
def search_virustotal(ioc_value, ioc_type):
    """
    Search for an IOC in VirusTotal and return the results.
    """
    api_key = next(vt_api_key_cycle)
    headers = {"x-apikey": api_key}
    url = ""

    # Determine endpoint based on IOC type
    if ioc_type == "file":
        url = f"https://www.virustotal.com/api/v3/files/{ioc_value}"
    elif ioc_type == "ip":
        url = f"https://www.virustotal.com/api/v3/ip_addresses/{ioc_value}"
    elif ioc_type == "url":
        url = f"https://www.virustotal.com/api/v3/urls/{ioc_value}"
    else:
        print("Unsupported IOC type for VirusTotal.")
        return {}

    print(f"Searching VirusTotal for {ioc_type.upper()}: {ioc_value}...")
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 404:
        print("No results found in VirusTotal.")
        return {}
    else:
        print(f"Error {response.status_code} from VirusTotal.")
        return {}

# Step 3: Format and Display Results
def display_results(otx_result, vt_result, ioc_value, ioc_type):
    """
    Display results in a human-readable format.
    """
    print("\n" + "=" * 50)
    print(f"Results for IOC: {ioc_value} ({ioc_type.upper()})")
    print("=" * 50)

    # OTX Results
    if otx_result:
        print("\n[OTX Results]")
        print(f"Pulse Count: {otx_result.get('pulse_info', {}).get('count', 0)}")
        for pulse in otx_result.get("pulse_info", {}).get("pulses", []):
            print(f" - Pulse Name: {pulse.get('name')}, Tags: {', '.join(pulse.get('tags', []))}")
    else:
        print("\n[OTX Results] No data found.")

    # VirusTotal Results
    if vt_result:
        print("\n[VirusTotal Results]")
        stats = vt_result.get("data", {}).get("attributes", {}).get("last_analysis_stats", {})
        print(f"Malicious: {stats.get('malicious', 0)}")
        print(f"Suspicious: {stats.get('suspicious', 0)}")
        print(f"Harmless: {stats.get('harmless', 0)}")
        print(f"Undetected: {stats.get('undetected', 0)}")

        if ioc_type == "file":
            hash_info = vt_result.get("data", {}).get("attributes", {})
            print(f"MD5: {hash_info.get('md5', 'N/A')}")
            print(f"SHA1: {hash_info.get('sha1', 'N/A')}")
            print(f"SHA256: {hash_info.get('sha256', 'N/A')}")
        elif ioc_type == "ip" or ioc_type == "url":
            print("VirusTotal Details:")
            print(json.dumps(vt_result.get("data", {}).get("attributes", {}), indent=4))
    else:
        print("\n[VirusTotal Results] No data found.")

# Step 4: Determine IOC Type
def determine_ioc_type(ioc_value):
    """
    Determines the type of IOC: file hash, IP address, or URL.
    """
    if re.match(r"\b[A-Fa-f0-9]{32}\b", ioc_value):  # MD5
        return "file"
    elif re.match(r"\b[A-Fa-f0-9]{40}\b", ioc_value):  # SHA1
        return "file"
    elif re.match(r"\b[A-Fa-f0-9]{64}\b", ioc_value):  # SHA256
        return "file"
    elif re.match(r"\b(?:\d{1,3}\.){3}\d{1,3}\b", ioc_value):  # IP Address
        return "ip"
    elif ioc_value.startswith("http://") or ioc_value.startswith("https://"):  # URL
        return "url"
    else:
        return None

# Step 5: Main Function
ioc_value = input("Enter the IOC (IP, hash, or URL): ").strip()
ioc_type = determine_ioc_type(ioc_value)

if not ioc_type:
  print("Invalid IOC format. Please enter a valid IP, hash, or URL.")

# Search in OTX and VirusTotal
otx_result = search_otx(ioc_value, ioc_type)
vt_result = search_virustotal(ioc_value, ioc_type)

# Display results
display_results(otx_result, vt_result, ioc_value, ioc_type)