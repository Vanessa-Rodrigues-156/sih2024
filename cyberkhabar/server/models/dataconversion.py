from neo4j import GraphDatabase
import json

# Load JSON data
data = json.loads('''[
  {
    "incident_name": "Mobikwik Data Breach",
    "date_of_incident": "2024-12-10T13:54:24.540655",
    "severity_level": "High",
    "affected_systems": "Mobile payment services",
    "threat_vector": "Data theft",
    "threat_actor": "Unknown",
    "mitre_attack_mapping": ["TA1059"],
    "indicators_of_compromise": [
      "Leaked KYC details of customers",
      "Leaked addresses",
      "Leaked phone numbers",
      "Leaked Aadhaar card details",
      "Leaked card details linked to MobiKwik Wallet"
    ],
    "data_impacted": "Over 3.5 million KYC details",
    "financial_operational_impact": "Potential financial losses due to data breaches and reputational damage",
    "response_actions_taken": [
      "Data audit conducted",
      "Third-party security review initiated"
    ],
    "recommended_mitigation": "Implement stricter security measures to protect sensitive customer data",
    "tlp_classification": "Confidential",
    "extra_relevant_information": {
      "number_of_merchants": 1.5 million,
      "number_of_customers": 55 million,
      "source_of_data_leak": "Dark web",
      "price_of_data_on_dark_web": "1.5 BTC or $85,000"
    }
  },
  {
    "incident_name": "Zomato Malware Attack",
    "date_of_incident": "2024-12-15T10:00:00.000000",
    "severity_level": "Medium",
    "affected_systems": "Food delivery services",
    "threat_vector": "Malware",
    "threat_actor": "Unknown",
    "mitre_attack_mapping": ["TA0002"],
    "indicators_of_compromise": [
      "Malicious software detected",
      "Unauthorized access attempts"
    ],
    "data_impacted": "Customer payment information",
    "financial_operational_impact": "Potential loss of customer trust",
    "response_actions_taken": [
      "Incident response team activated",
      "User  notifications sent"
    ],
    "recommended_mitigation": "Enhance malware detection systems",
    "tlp_classification": "Confidential",
    "extra_relevant_information": {
      "number_of_merchants": 1 million,
      "number_of_customers": 50 million,
      "source_of_data_leak": "Unknown",
      "price_of_data_on_dark_web": "N/A"
    }
  }
]''')

# Connect to Neo4j
driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "password"))

def create_incident(tx, incident):
    # Create incident node
    tx.run("""
        CREATE (i:Incident {
            name: $name,
            date: $date,
            severity: $severity,
            affected_systems: $affected_systems,
            threat_vector: $threat_vector,
            threat_actor: $threat_actor,
            data_impacted: $data_impacted,
            financial_impact: $financial_impact,
            recommended_mitigation: $recommended_mitigation
        })
    """, name=incident['incident_name'], date=incident['date_of_incident'], 
    severity=incident['severity_level'], affected_systems=incident['affected_systems'], 
    threat_vector=incident['threat_vector'], threat_actor=incident['threat_actor'], 
    data_impacted=incident['data_impacted'], 
    financial_impact=incident['financial_operational_impact'], 
    recommended_mitigation=incident['recommended_mitigation'])

def create_relationships(tx, incident):
    # Create relationships based on common parameters
    for other_incident in data:
        if incident['threat_vector'] == other_incident['threat_vector'] and incident['incident_name'] != other_incident['incident_name']:
            tx.run("""
                MATCH (i1:Incident {name: $name1}), (i2:Incident {name: $name2})
                CREATE (i1)-[:RELATED_TO {type: 'THREAT_VECTOR'}]->(i2)
            """, name1=incident['incident_name'], name2=other_incident['incident_name'])

with driver.session() as session:
    for incident in data:
        session.write_transaction(create_incident, incident)
        session.write_transaction(create_relationships, incident)

driver.close()