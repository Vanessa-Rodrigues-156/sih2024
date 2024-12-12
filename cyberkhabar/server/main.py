from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from neo4j import GraphDatabase
from pydantic import BaseModel
from typing import List, Dict
import json
import uvicorn

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
AUTH = ("neo4j", "QWERTYUIOP0")  # Replace with your credentials

def get_db():
    return GraphDatabase.driver(URI, auth=AUTH)



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
@app.get("/api/incidents")
async def readdata():
    data={
        "attackTypes": ["Ransomware", "Phishing", "DDoS", "Malware"],
        "impactLevels": ["High", "Medium", "Low"],
        "locations": ["North America", "Europe", "Asia"],
        "selectedFilters": {
        "type": [],
        "impact": [],
        "location": [],
        "recency": "7"
        },
        "news": [
        {
            "id": 1,
            "title": "Ransomware Attack on Healthcare",
            "description": "A major ransomware attack has affected healthcare facilities...",
            
        },
        {
            "id": 2,
            "title": "Phishing Campaign Targets Banks",
            "description": "A new phishing campaign is targeting major banks...",
           
        },
        {
            "id": 3,
            "title": "DDoS Attack on Government Websites",
            "description": "Government websites have been hit by a DDoS attack...",
         
        }
        ],
        "currentStats": {
        "Active Threats": 5,
        "Resolved Incidents": 12,
        "Pending Alerts": 3,
        "relatedIncidents": 20
        }
        }
    return data   

    
    
class SignupRequest(BaseModel):
    username: str
    password: str
    email: str



@app.post("/api/auth/signup")
async def signup(request: SignupRequest):
    # Here you would typically add logic to save the user to a database
    # For demonstration, we'll assume the signup is always successful

    # Return a positive response
    return {"message": "Signup successful", "username": request.username}

@app.post("/api/auth/login")
async def login(request: SignupRequest):
    # Here you would typically add logic to save the user to a database
    # For demonstration, we'll assume the signup is always successful

    # Return a positive response
    return {"message": "Login successful", "username": request.username}

# Add more endpoints as needed

@app.get("/api/incidents/{incident_id}", response_model=Dict)
async def read_incident(incident_id: str):
    try:
        with get_db().session() as session:
            result = session.run("MATCH (i:Incident) WHERE id(i) = $incident_id RETURN i", incident_id=int(incident_id))
            record = result.single()
            if record is None:
                raise HTTPException(status_code=404, detail="Incident not found")
            
            # Convert the Neo4j Node to a dictionary
            incident_node = record["i"]
            incident_data = {
                "identity": incident_node.id,
                "labels": list(incident_node.labels),
                "properties": dict(incident_node)
            }
        return incident_data
    except :
        raise HTTPException(status_code=503, detail="Service Unavailable")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5001)