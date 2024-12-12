import json
import os
import logging
from typing import List, Dict, Any
import neo4j
from datetime import datetime

class CyberIncidentImporter:
    def __init__(self, 
                 neo4j_uri: str, 
                 neo4j_username: str, 
                 neo4j_password: str,
                 log_file: str = 'cyber_incident_importer.log'):
        """
        Initialize Neo4j driver and logging for cyber incident import
        
        :param neo4j_uri: Neo4j database connection URI
        :param neo4j_username: Neo4j database username
        :param neo4j_password: Neo4j database password
        :param log_file: Path to log file
        """
        # Neo4j connection
        self._driver = neo4j.GraphDatabase.driver(
            neo4j_uri, 
            auth=(neo4j_username, neo4j_password)
        )
        
        # Logging configuration
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s: %(message)s',
            filename=log_file,
            filemode='a'
        )
        self.logger = logging.getLogger(__name__)

    def validate_incident_data(self, incident: Dict[str, Any]) -> bool:
        """
        Validate the structure of an incident JSON
        
        :param incident: Incident dictionary to validate
        :return: Boolean indicating if incident data is valid
        """
        required_keys = [
            'Incident Name', 
            'Date of Incident', 
            'Severity Level',
            'Affected Systems',
            'Threat Vector'
        ]
        
        for key in required_keys:
            if key not in incident or not incident[key]:
                self.logger.warning(f"Missing required key: {key}")
                return False
        
        return True

    def import_incidents(self, incidents: List[Dict[str, Any]]):
        """
        Import a list of cyber incidents into Neo4j graph database
        
        :param incidents: List of incident dictionaries
        """
        with self._driver.session() as session:
            for incident in incidents:
                try:
                    # Validate incident data
                    if not self.validate_incident_data(incident):
                        self.logger.warning(f"Skipping invalid incident: {incident.get('Incident Name', 'Unknown')}")
                        continue

                    # Create or merge Incident node
                    create_incident_query = """
                    MERGE (i:Incident {name: $name})
                    SET 
                        i.date = $date,
                        i.severity = $severity,
                        i.affectedSystems = $affectedSystems,
                        i.threatVector = $threatVector,
                        i.tlpClassification = $tlpClassification,
                        i.dataImpacted = $dataImpacted,
                        i.financialImpact = $financialImpact,
                        i.responseActions = $responseActions,
                        i.recommendedMitigation = $recommendedMitigation
                    RETURN i
                    """
                    
                    # Prepare incident data
                    incident_data = {
                        'name': incident.get('Incident Name', 'Unknown Incident'),
                        'date': incident.get('Date of Incident', 'Unknown Date'),
                        'severity': incident.get('Severity Level', 'Unclassified'),
                        'affectedSystems': incident.get('Affected Systems', 'N/A'),
                        'threatVector': incident.get('Threat Vector', 'Unknown'),
                        'tlpClassification': incident.get('TLP Classification', 'WHITE'),
                        'dataImpacted': incident.get('Data Impacted', 'N/A'),
                        'financialImpact': incident.get('Financial/Operational Impact', 'N/A'),
                        'responseActions': incident.get('Response Actions Taken', 'No actions recorded'),
                        'recommendedMitigation': incident.get('Recommended Mitigation', 'No recommendations')
                    }
                    
                    # Execute main incident node creation
                    session.run(create_incident_query, incident_data)

                    # Process MITRE ATT&CK Tactics
                    self._process_mitre_tactics(session, incident)

                    # Process Threat Actors
                    self._process_threat_actors(session, incident)

                    # Process Indicators of Compromise
                    self._process_iocs(session, incident)

                    # Link Incident to Severity Level
                    self._link_severity_level(session, incident)

                    self.logger.info(f"Successfully imported incident: {incident.get('Incident Name')}")

                except Exception as e:
                    self.logger.error(f"Error importing incident {incident.get('Incident Name')}: {e}")
                    # Optionally, you could add error handling logic here

    def _process_mitre_tactics(self, session, incident):
        """
        Create MITRE ATT&CK Tactics nodes and link to incident
        """
        tactics = incident.get('MITRE ATT&CK Mapping', '').split(', ')
        for tactic in tactics:
            if tactic:
                tactic_query = """
                MERGE (t:MITRETactic {name: $name})
                WITH t
                MATCH (i:Incident {name: $incident_name})
                MERGE (i)-[:USES_TACTIC]->(t)
                """
                session.run(tactic_query, {
                    'name': tactic,
                    'incident_name': incident.get('Incident Name')
                })

    def _process_threat_actors(self, session, incident):
        """
        Create Threat Actor nodes and link to incident
        """
        threat_actor = incident.get('Threat Actor (if known)', '').strip()
        if threat_actor and threat_actor.lower() != 'unknown':
            actor_query = """
            MERGE (a:ThreatActor {name: $name})
            WITH a
            MATCH (i:Incident {name: $incident_name})
            MERGE (i)-[:ATTRIBUTED_TO]->(a)
            """
            session.run(actor_query, {
                'name': threat_actor,
                'incident_name': incident.get('Incident Name')
            })

    def _process_iocs(self, session, incident):
        """
        Create Indicators of Compromise nodes and link to incident
        """
        iocs = incident.get('Indicators of Compromise (IoCs)', '').split(', ')
        for ioc in iocs:
            if ioc:
                ioc_query = """
                MERGE (ioc:IoC {value: $value})
                WITH ioc
                MATCH (i:Incident {name: $incident_name})
                MERGE (i)-[:HAS_IOC]->(ioc)
                """
                session.run(ioc_query, {
                    'value': ioc,
                    'incident_name': incident.get('Incident Name')
                })

    def _link_severity_level(self, session, incident):
        """
        Link Incident to its Severity Level
        """
        severity_query = """
        MATCH (i:Incident {name: $incident_name})
        MERGE (s:SeverityLevel {level: $severity})
        MERGE (i)-[:HAS_SEVERITY]->(s)
        """
        session.run(severity_query, {
            'incident_name': incident.get('Incident Name'),
            'severity': incident.get('Severity Level', 'Unclassified')
        })

    def close(self):
        """Close the Neo4j database connection"""
        self._driver.close()

def load_json_data(file_path: str) -> List[Dict[str, Any]]:
    """
    Load JSON data from a file
    
    :param file_path: Path to the JSON file
    :return: List of incident dictionaries
    """
    try:
        with open(file_path, 'r') as file:
            # Attempt to parse the data key if it exists
            data = json.load(file)
            incidents = data.get('data', data) if isinstance(data, dict) else data
            
            # Ensure we have a list of incidents
            if not isinstance(incidents, list):
                raise ValueError("Invalid JSON structure: Expected a list of incidents")
            
            return incidents
    except json.JSONDecodeError as e:
        logging.error(f"JSON Decode Error: {e}")
        return []
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        return []

def main():
    # Configuration (replace with your actual details)
    NEO4J_URI = os.getenv('NEO4J_URI', 'bolt://localhost:7687')
    NEO4J_USERNAME = os.getenv('NEO4J_USERNAME', 'neo4j')
    NEO4J_PASSWORD = os.getenv('NEO4J_PASSWORD', 'QWERRTYUIOP')
    
    # File path (replace with your actual JSON file path)
    JSON_FILE_PATH = 'cyber_incidents.json'

    # Create importer
    importer = CyberIncidentImporter(
        NEO4J_URI, 
        NEO4J_USERNAME, 
        NEO4J_PASSWORD
    )

    try:
        # Load incidents from JSON
        incidents = load_json_data(JSON_FILE_PATH)
        
        if not incidents:
            print("No incidents found in the JSON file.")
            return

        # Import incidents
        importer.import_incidents(incidents)
        print(f"Successfully processed {len(incidents)} incidents.")

    except Exception as e:
        print(f"Error during import: {e}")
    finally:
        # Always close the connection
        importer.close()

if __name__ == "__main__":
    main()
