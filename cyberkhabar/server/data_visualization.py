from neo4j import GraphDatabase
import matplotlib.pyplot as plt

# Replace with your Neo4j connection details
uri = "bolt://localhost:7687"
user = "neo4j"
password = "your_password"

# Connect to Neo4j
driver = GraphDatabase.driver(uri, auth=(user, password))

# Dummy data
line_data = [
    {"x": 1, "y": 5},
    {"x": 2, "y": 8},
    {"x": 3, "y": 3},
    {"x": 4, "y": 10},
    {"x": 5, "y": 6}
]

# Function to create data in Neo4j
def create_data_in_neo4j(tx, data, label):
    for point in data:
        tx.run(
            f"CREATE (n:{label} {{x: $x, y: $y}})",
            x=point["x"],
            y=point["y"]
        )

# Write data to Neo4j
with driver.session() as session:
    session.write_transaction(create_data_in_neo4j, line_data, "Line")

# Read data from Neo4j
def read_data_from_neo4j(tx, label):
    result = tx.run(f"MATCH (n:{label}) RETURN n.x AS x, n.y AS y")
    return [{"x": record["x"], "y": record["y"]} for record in result]

with driver.session() as session:
    line_data_from_db = session.read_transaction(read_data_from_neo4j, "Line")

# Extract x and y values
x_values = [point["x"] for point in line_data_from_db]
y_values = [point["y"] for point in line_data_from_db]

# Plot the data
plt.plot(x_values, y_values, marker='o')
plt.title('Sample Line Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
plt.show()

# Close the driver connection
driver.close()