import json
import logging
from neo4j import GraphDatabase, basic_auth
from neo4j.exceptions import Neo4jError

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

# Neo4j connection configuration
URI = "bolt://localhost:7687"
USERNAME = "neo4j"
PASSWORD = "your_password"  # Replace with your Neo4j password


class Neo4jHandler:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=basic_auth(user, password))

    def close(self):
        self.driver.close()

    def create_incident(self, incident):
        with self.driver.session() as session:
            session.execute_write(self._create_and_return_incident, incident)
            self._create_relationships(session, incident)

    @staticmethod
    def _create_and_return_incident(tx, incident):
        query = """
        CREATE (i:Incident {
            incident_name: $incident_name,
            date_of_incident: date($date_of_incident),
            severity_level: $severity_level,
            threat_vector: $threat_vector,
            threat_actor: $threat_actor,
            financial_operational_impact: $financial_operational_impact,
            tlp_classification: $tlp_classification
        })
        RETURN i
        """
        result = tx.run(
            query,
            incident_name=incident["incident_name"],
            date_of_incident=incident["date_of_incident"],
            severity_level=incident["severity_level"],
            threat_vector=incident["threat_vector"],
            threat_actor=incident["threat_actor"],
            financial_operational_impact=incident["financial_operational_impact"],
            tlp_classification=incident["tlp_classification"],
        )
        return result.single()

    def _create_relationships(self, session, incident):
        incident_name = incident["incident_name"]

        # Affected Systems
        for system in incident["affected_systems"]:
            session.execute_write(
                self._create_system_relationship, incident_name, system
            )

        # MITRE ATT&CK Mappings
        for mitre in incident["mitre_attck_mapping"]:
            session.execute_write(self._create_mitre_relationship, incident_name, mitre)

        # IOCs
        iocs = incident.get("iocs", {})
        for ioc_type, ioc_values in iocs.items():
            for ioc in ioc_values:
                session.execute_write(
                    self._create_ioc_relationship, incident_name, ioc_type, ioc
                )

        # Threat Actor
        session.execute_write(
            self._create_threat_actor_relationship,
            incident_name,
            incident["threat_actor"],
        )

        # Data Impacted
        for data in incident["data_impacted"]:
            session.execute_write(
                self._create_data_impacted_relationship, incident_name, data
            )

        # Response Actions Taken
        for action in incident["response_actions_taken"]:
            session.execute_write(
                self._create_response_action_relationship, incident_name, action
            )

        # Recommended Mitigation
        for mitigation in incident["recommended_mitigation"]:
            session.execute_write(
                self._create_recommended_mitigation_relationship,
                incident_name,
                mitigation,
            )

    @staticmethod
    def _create_system_relationship(tx, incident_name, system):
        query = """
        MERGE (i:Incident {incident_name: $incident_name})
        MERGE (s:System {name: $system})
        MERGE (i)-[:AFFECTED_SYSTEM]->(s)
        """
        tx.run(query, incident_name=incident_name, system=system)

    @staticmethod
    def _create_mitre_relationship(tx, incident_name, mitre):
        query = """
        MERGE (i:Incident {incident_name: $incident_name})
        MERGE (m:MITREAttack {id: $mitre_id})
        MERGE (i)-[:MITRE_MAPPING]->(m)
        """
        tx.run(query, incident_name=incident_name, mitre_id=mitre)

    @staticmethod
    def _create_ioc_relationship(tx, incident_name, ioc_type, ioc):
        query = """
        MERGE (i:Incident {incident_name: $incident_name})
        MERGE (ioc:IOC {type: $ioc_type, value: $ioc})
        MERGE (i)-[:HAS_IOC]->(ioc)
        """
        tx.run(query, incident_name=incident_name, ioc_type=ioc_type, ioc=ioc)

    @staticmethod
    def _create_threat_actor_relationship(tx, incident_name, threat_actor):
        query = """
        MERGE (i:Incident {incident_name: $incident_name})
        MERGE (ta:ThreatActor {name: $threat_actor})
        MERGE (i)-[:INVOLVED_THREAT_ACTOR]->(ta)
        """
        tx.run(query, incident_name=incident_name, threat_actor=threat_actor)

    @staticmethod
    def _create_data_impacted_relationship(tx, incident_name, data):
        query = """
        MERGE (i:Incident {incident_name: $incident_name})
        MERGE (d:DataImpacted {name: $data})
        MERGE (i)-[:IMPACTED_DATA]->(d)
        """
        tx.run(query, incident_name=incident_name, data=data)

    @staticmethod
    def _create_response_action_relationship(tx, incident_name, action):
        query = """
        MERGE (i:Incident {incident_name: $incident_name})
        MERGE (ra:ResponseAction {description: $action})
        MERGE (i)-[:RESPONSE_ACTION_TAKEN]->(ra)
        """
        tx.run(query, incident_name=incident_name, action=action)

    @staticmethod
    def _create_recommended_mitigation_relationship(tx, incident_name, mitigation):
        query = """
        MERGE (i:Incident {incident_name: $incident_name})
        MERGE (rm:RecommendedMitigation {description: $mitigation})
        MERGE (i)-[:RECOMMENDED_MITIGATION]->(rm)
        """
        tx.run(query, incident_name=incident_name, mitigation=mitigation)


def main():
    # Initialize Neo4j handler
    neo4j_handler = Neo4jHandler(URI, USERNAME, PASSWORD)

    try:
        # Load data from JSON
        with open("data.json", "r") as f:
            data = json.load(f)

        for incident in data:
            # Create Incident node and related relationships
            neo4j_handler.create_incident(incident)
            logging.info(
                f"Created incident and relationships: {incident['incident_name']}"
            )

    except Neo4jError as e:
        logging.error(f"Neo4j error: {e}")

    except Exception as e:
        logging.error(f"Error: {e}")

    finally:
        neo4j_handler.close()


if __name__ == "__main__":
    main()
