from neo4j import GraphDatabase

class IncidentCounter:

    def _init_(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def count_incident_nodes(self):
        with self.driver.session() as session:
            result = session.run(
                """
                MATCH (n:Incident)
                RETURN count(n) AS incident_count
                """
            )
            incident_count = result.single()["incident_count"]
            print(f"Number of incident nodes: {incident_count}")

    def count_incident_nodes_with_properties(self):
        with self.driver.session() as session:
            result = session.run(
                """
                MATCH (n:Incident)
                WHERE exists(n.property1) AND exists(n.property2)  // Replace with actual property names
                RETURN count(n) AS incident_count_with_properties
                """
            )
            incident_count_with_properties = result.single()["incident_count_with_properties"]
            print(f"Number of incident nodes with properties: {incident_count_with_properties}")

    def count_incident_nodes_with_relations(self):
        with self.driver.session() as session:
            result = session.run(
                """
                MATCH (n:Incident)-[r]->()
                RETURN count(DISTINCT n) AS incident_count_with_relations
                """
            )
            incident_count_with_relations = result.single()["incident_count_with_relations"]
            print(f"Number of incident nodes with relations: {incident_count_with_relations}")

if __name__ == "__main__":
    uri = "bolt://localhost:7687"  # Replace with your Neo4j URI
    user = "neo4j"  # Replace with your Neo4j username
    password = "QWERTYUIOP0"  # Replace with your Neo4j password

    counter = IncidentCounter(uri, user, password)
    counter.count_incident_nodes()
    counter.count_incident_nodes_with_properties()
    counter.count_incident_nodes_with_relations()
    print(counter)
   # counter.close()