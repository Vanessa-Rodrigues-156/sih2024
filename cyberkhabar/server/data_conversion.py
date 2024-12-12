import json
from neo4j import GraphDatabase

# Neo4j connection configuration
URI = "bolt://localhost:7687"
AUTH = ("neo4j", "QWERTYUIOP0")  # Replace with your credentials

def get_db():
    return GraphDatabase.driver(URI, auth=AUTH)

def import_incidents(incidents):
    with get_db().session() as session:
        for incident in incidents:
            session.run("""
                CREATE (i:Incident {
                    incident_name: $incident_name,
                    date_of_incident: $date_of_incident,
                    severity_level: $severity_level,
                    affected_systems: $affected_systems,
                    threat_vector: $threat_vector,
                    threat_actor: $threat_actor,
                    mitre_attck_mapping: $mitre_attck_mapping,
                    iocs: $iocs,
                    data_impacted: $data_impacted,
                    financial_operational_impact: $financial_operational_impact,
                    response_actions_taken: $response_actions_taken,
                    recommended_mitigation: $recommended_mitigation,
                    tlp_classification: $tlp_classification
                })
            """, incident)

def main():
    # Replace this with the path to your JSON file
    json_file_path = "data.json"

    try:
        with open(json_file_path, "r") as file:
            incidents = json.load(file)

        # Import incidents
        import_incidents(incidents)
        print(f"Successfully processed {len(incidents)} incidents.")

    except Exception as e:
        print(f"Error during import: {e}")
    finally:
        # Always close the connection
        get_db().close()

if __name__ == "__main__":
    main()