from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from neo4j import GraphDatabase
import json

app = FastAPI()

# Load JSON data from a file
with open('data.json', 'r') as file:
    data = json.load(file)

# Connect to Neo4j
driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "CPAT5OChnHp6cXhaHmyzitohnQsGh6ucx4b7b13jwck"))

class Incident(BaseModel):
    incident_name: str
    date_of_incident: str
    severity_level: str
    affected_systems: str
    threat_vector: str
    threat_actor: str
    data_impacted: str
    financial_operational_impact: str
    recommended_mitigation: str

def create_incident(tx, incident):
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
    """, name=incident.incident_name, date=incident.date_of_incident, 
    severity=incident.severity_level, affected_systems=incident.affected_systems, 
    threat_vector=incident.threat_vector, threat_actor=incident.threat_actor, 
    data_impacted=incident.data_impacted, 
    financial_impact=incident.financial_operational_impact, 
    recommended_mitigation=incident.recommended_mitigation)

@app.post("/incidents/")
async def add_incident(incident: Incident):
    try:
        with driver.session(database="maindb") as session:
            session.execute_write(create_incident, incident)
        return {"message": "Incident created successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/incidents/")
async def get_incidents():
    try:
        with driver.session(database="maindb") as session:
            result = session.run("MATCH (i:Incident) RETURN i")
            incidents = [record["i"] for record in result]
        return incidents
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/incidents/{incident_name}")
async def get_incident(incident_name: str):
    try:
        with driver.session(database="maindb") as session:
            result = session.run("MATCH (i:Incident {name: $name}) RETURN i", name=incident_name)
            incident = result.single()
            if incident:
                return incident["i"]
            else:
                raise HTTPException(status_code=404, detail="Incident not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.on_event("shutdown")
def shutdown_event():
    driver.close()