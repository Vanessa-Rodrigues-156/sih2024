import json
import neo4j
from datetime import datetime
import logging

class DetailedIncidentImporter:
    def _init_(self, neo4j_uri, neo4j_username, neo4j_password):
        """
        Initialize Neo4j driver and logging
        """
        self._driver = neo4j.GraphDatabase.driver(
            neo4j_uri, 
            auth=(neo4j_username, neo4j_password)
        )
        
        # Configure logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s: %(message)s'
        )
        self.logger = logging.getLogger(__name__)

    def parse_and_import_incident(self, incident_json):
        """
        Parse detailed incident JSON and import into Neo4j graph database
        """
        with self._driver.session() as session:
            try:
                # Create or merge the main Incident node
                incident_query = """
                MERGE (i:Incident {name: $name})
                SET 
                    i.date = $date,
                    i.severity = $severity,
                    i.affectedSystems = $affectedSystems,
                    i.threatVector = $threatVector,
                    i.dataImpacted = $dataImpacted,
                    i.financialImpact = $financialImpact,
                    i.responseActions = $responseActions,
                    i.recommendedMitigation = $recommendedMitigation,
                    i.tlpClassification = $tlpClassification
                RETURN i
                """
                
                # Prepare incident data
                incident_data = {
                    'name': incident_json.get('Incident Name'),
                    'date': incident_json.get('Date of Incident'),
                    'severity': incident_json.get('Severity Level'),
                    'affectedSystems': incident_json.get('Affected Systems'),
                    'threatVector': incident_json.get('Threat Vector'),
                    'dataImpacted': incident_json.get('Data Impacted'),
                    'financialImpact': incident_json.get('Financial/Operational Impact'),
                    'responseActions': incident_json.get('Response Actions Taken'),
                    'recommendedMitigation': incident_json.get('Recommended Mitigation'),
                    'tlpClassification': incident_json.get('TLP Classification')
                }
                
                # Execute main incident node creation
                session.run(incident_query, incident_data)
                
                # Create Threat Actor node and relationship if known
                threat_actor = incident_json.get('Threat Actor (if known)', '').strip()
                if threat_actor:
                    actor_query = """
                    MERGE (a:ThreatActor {name: $name})
                    WITH a
                    MATCH (i:Incident {name: $incident_name})
                    MERGE (i)-[:ATTRIBUTED_TO]->(a)
                    """
                    session.run(actor_query, {
                        'name': threat_actor,
                        'incident_name': incident_json.get('Incident Name')
                    })
                
                # Create MITRE ATT&CK Tactics nodes
                mitre_tactics = incident_json.get('MITRE ATT&CK Mapping', '').split(', ')
                for tactic in mitre_tactics:
                    if tactic:
                        tactic_query = """
                        MERGE (t:MITRETactic {name: $name})
                        WITH t
                        MATCH (i:Incident {name: $incident_name})
                        MERGE (i)-[:USES_TACTIC]->(t)
                        """
                        session.run(tactic_query, {
                            'name': tactic,
                            'incident_name': incident_json.get('Incident Name')
                        })
                
                # Create IoCs nodes
                iocs = incident_json.get('Indicators of Compromise (IoCs)', '').split(', ')
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
                            'incident_name': incident_json.get('Incident Name')
                        })
                
                # Link Incident to its Severity Level
                severity_query = """
                MATCH (i:Incident {name: $incident_name})
                MERGE (s:SeverityLevel {level: $severity})
                MERGE (i)-[:HAS_SEVERITY]->(s)
                """
                session.run(severity_query, {
                    'incident_name': incident_json.get('Incident Name'),
                    'severity': incident_json.get('Severity Level', 'Unclassified')
                })

                self.logger.info(f"Successfully imported incident: {incident_json.get('Incident Name')}")

            except Exception as e:
                self.logger.error(f"Error importing incident: {e}")
                raise

    def close(self):
        """Close the Neo4j database connection"""
        self._driver.close()

def main():
    # Configuration (replace with your actual Neo4j details)
    NEO4J_URI = 'bolt://localhost:7687'
    NEO4J_USERNAME = 'neo4j'
    NEO4J_PASSWORD = 'QWERTYUUIOP0'

    # Sample incident JSON
    incident_json = {
        "Incident Name": "MSEB Cyber Attack",
        "Date of Incident": "October 12, 2020",
        "Severity Level": "High",
        "Affected Systems": "Power grid, transmission systems",
        "Threat Vector": "Malware",
        "Threat Actor (if known)": "Suspected Chinese state-sponsored group Red Echo",
        "MITRE ATT&CK Mapping": "Initial Access, Execution",
        "Indicators of Compromise (IoCs)": "14 Trojan Horses, unauthorized access, 8GB of unaccounted data",
        "Data Impacted": "Power grid operations, transmission data",
        "Financial/Operational Impact": "Massive power outage in Mumbai, disruption to financial and stock markets",
        "Response Actions Taken": "Forensic investigation, system isolation, collaboration with cybersecurity experts",
        "Recommended Mitigation": "Enhanced monitoring, multi-factor authentication, regular security audits",
        "TLP Classification": "RED"
    }

    # Create importer
    importer = DetailedIncidentImporter(NEO4J_URI, NEO4J_USERNAME, NEO4J_PASSWORD)

    try:
        # Import the incident
        importer.parse_and_import_incident(incident_json)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        importer.close()

if __name__ == "_main_":
    main()