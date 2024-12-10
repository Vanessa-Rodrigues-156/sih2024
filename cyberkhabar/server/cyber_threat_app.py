import openai
import json
from neo4j import GraphDatabase

# Step 1: LLM Function to Extract Data
def extract_incident_data(prompt_text, api_key):
    openai.api_key = api_key
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an expert cybersecurity analyst."},
            {"role": "user", "content": prompt_text},
        ]
    )
    return response['choices'][0]['message']['content']

# Step 2: Create JSON for Neo4j
def create_incident_json(data):
    structured_data = {
        "date_of_incident": data.get("Date of Incident", ""),
        "target_company": data.get("Target Company", ""),
        "headline_overview": data.get("Headline and Overview", ""),
        "type_of_attack": data.get("Type of Attack", ""),
        "impact": data.get("Impact", ""),
        "response": data.get("Response", ""),
        "financial_impact": data.get("Financial Impact", ""),
    }
    with open("incident_data.json", "w") as file:
        json.dump(structured_data, file, indent=4)
    print("Data written to incident_data.json")
    return structured_data

# Step 3: Upload to Neo4j
class Neo4jUploader:
    def _init_(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def create_cyber_incident(self, incident_data):
        with self.driver.session() as session:
            session.write_transaction(self._create_nodes_and_relationships, incident_data)

    @staticmethod
    def _create_nodes_and_relationships(tx, data):
        query = """
        CREATE (incident:Incident {
            name: $headline_overview,
            date: $date_of_incident,
            type: $type_of_attack,
            impact: $impact,
            response: $response,
            financialImpact: $financial_impact
        })
        MERGE (company:Company {name: $target_company})
        MERGE (incident)-[:TARGETED]->(company)
        """
        tx.run(query, **data)

# Step 4: Execution Workflow
if _name_ == "_main_":
    # Input: Unstructured Text
    unstructured_text = """
    On December 5, 2024, CompanyX experienced a ransomware attack. The attackers encrypted critical customer data,
    demanding a $10 million ransom. The breach exposed 2 million customer records, leading to significant reputational damage.
    """

    # Prompt for the LLM
    prompt = f"""
    Extract the following details from this text:
    - Date of Incident
    - Target Company
    - Headline and Overview
    - Type of Attack
    - Impact
    - Response
    - Financial Impact
    Text: {unstructured_text}
    """

    # Step 1: Extract Data
    api_key = "your_openai_api_key"
    extracted_data = extract_incident_data(prompt, api_key)
    print("Extracted Data:", extracted_data)

    # Step 2: Create JSON
    extracted_data_dict = json.loads(extracted_data)  # Convert string response to a dictionary
    structured_data = create_incident_json(extracted_data_dict)

    # Step 3: Upload to Neo4j
    uri = "bolt://localhost:7687"  # Adjust as needed
    username = "neo4j"
    password = "your_neo4j_password"

    uploader = Neo4jUploader(uri, username, password)
    uploader.create_cyber_incident(structured_data)
    uploader.close()

    print("Data uploaded to Neo4j.")