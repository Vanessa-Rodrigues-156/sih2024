from neo4j import GraphDatabase, RoutingControl


URI = "neo4j://localhost:7687"
AUTH = ("neo4j", "CPAT5OChnHp6cXhaHmyzitohnQsGh6ucx4b7b13jwck")


def add_friend(driver, name, friend_name):
    driver.execute_query(
        "MERGE (a:Person {name: $name}) "
        "MERGE (friend:Person {name: $friend_name}) "
        "MERGE (a)-[:KNOWS]->(friend)",
        name=name, friend_name=friend_name, database_="maindb",
    )


def print_friends(driver, name):
    if not name:
        raise Exception("Name is required")
    results = driver.execute_query(
        "MATCH (a:Person)-[:KNOWS]->(friend) WHERE a.name = $name "
        "RETURN friend.name ORDER BY friend.name",
        name=name, database_="neo4j", routing_=RoutingControl.READ,
    )
    for record in results:
        print(record["friend.name"])
    return results if results else "no friends"
  

with GraphDatabase.driver(URI, auth=AUTH) as driver:
    add_friend(driver, "Amyra", "Guinevere")
    add_friend(driver, "Arthur", "Shawny")
    add_friend(driver, "Arthur", "Amyra")
    print_friends(driver, "shawny")