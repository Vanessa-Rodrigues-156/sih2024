from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from neo4j import GraphDatabase, ServiceUnavailable
from pydantic import BaseModel
from typing import List
import json

app = FastAPI()

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Neo4j connection configuration
URI = "bolt://localhost:7687"
AUTH = ("neo4j", "your_password")  # Replace with your credentials

def get_db():
    return GraphDatabase.driver(URI, auth=AUTH)

@app.on_event("startup")
async def startup_event():
    try:
        with get_db().session() as session:
            session.run("RETURN 1")
        print("Connected to Neo4j")
    except ServiceUnavailable:
        raise HTTPException(status_code=503, detail="Service Unavailable")

@app.on_event("shutdown")
async def shutdown_event():
    get_db().close()

# Define your data models
class Incident(BaseModel):
    incident_name: str
    date_of_incident: str
    severity_level: str
    affected_systems: str
    threat_vector: str
    threat_actor: str
    mitre_attck_mapping: str
    iocs: str
    data_impacted: str
    financial_operational_impact: str
    response_actions_taken: str
    recommended_mitigation: str
    tlp_classification: str

# Define your API endpoints
@app.post("/api/incidents")
async def create_incident(incident: Incident):
    with get_db().session() as session:
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
        """, incident.dict())
    return {"status": "success"}

# Add more endpoints as needed

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5001)