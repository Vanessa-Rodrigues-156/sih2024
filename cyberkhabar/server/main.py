from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from neo4j import GraphDatabase
from pydantic import BaseModel
from typing import List
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
@app.post("/api/incidents")
async def create_incident(incident: Incident):
    with get_db().session() as session:
         result = session.run("MATCH (i:Incident) RETURN i")
         incidents= [record["i"] for record in result]
         

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

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5001)