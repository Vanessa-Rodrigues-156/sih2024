from neo4j import GraphDatabase
import json

# Load JSON data from a file
with open('data.json', 'r') as file:
    data = json.load(file)

# Ensure data is a dictionary
if not isinstance(data, dict):
    raise TypeError("Data must be a dictionary")

# Connect to Neo4j
driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "CPAT5OChnHp6cXhaHmyzitohnQsGh6ucx4b7b13jwck"))

def create_incident(tx, incident):
    # Create incident node
    tx.run("""
        CREATE (i:Incident {
            name: $name,
            date: $date,
            location: $location,
            target: $target,
            amount_siphoned: $amount_siphoned,
            transactions: $transactions,
            other_damage: $other_damage,
            vulnerability: $vulnerability,
            police_report: $police_report,
            legal_action: $legal_action,
            bank_action: $bank_action
        })
    """, name=incident['Incident Name'], date=incident['Date of Incident'], 
    location=incident['Location'], target=incident['Target'], 
    amount_siphoned=incident['Impact']['Amount siphoned'], 
    transactions=incident['Impact']['Transactions'], 
    other_damage=incident['Impact']['Other damage'], 
    vulnerability=incident['Vulnerability'], 
    police_report=incident['Response']['Police report'], 
    legal_action=incident['Response']['Legal action'], 
    bank_action=incident['Response']['Bank action'])

def create_prevention_actions(tx, incident):
    # Create prevention actions nodes and relationships
    for action in incident['Prevention']['Recommended actions']:
        tx.run("""
            MATCH (i:Incident {name: $name})
            CREATE (p:PreventionAction {action: $action})
            CREATE (i)-[:RECOMMENDED]->(p)
        """, name=incident['Incident Name'], action=action)

def create_methodology(tx, incident):
    # Create methodology nodes and relationships
    for method in incident['Methodology']['Malware usage']:
        tx.run("""
            MATCH (i:Incident {name: $name})
            CREATE (m:Methodology {method: $method})
            CREATE (i)-[:USED]->(m)
        """, name=incident['Incident Name'], method=method)

try:
    with driver.session(database="maindb") as session:  # Specify the database name here
        session.execute_write(create_incident, data)
        session.execute_write(create_prevention_actions, data)
        session.execute_write(create_methodology, data)
finally:
    driver.close()