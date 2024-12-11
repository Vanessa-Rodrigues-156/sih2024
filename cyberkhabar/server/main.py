from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from neo4j import GraphDatabase

app = FastAPI()

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database connection
driver = GraphDatabase.driver(
    "neo4j://localhost:7687",
    auth=("neo4j", "password")
)

# Models
class Incident(BaseModel):
    title: str
    severity: str
    sector: str
    description: str
    timestamp: datetime

class Alert(BaseModel):
    name: str
    message: str
    timestamp: datetime

# Routes
@app.get("/dashboard/stats")
async def get_dashboard_stats():
    with driver.session() as session:
        result = session.run("""
            MATCH (i:Incident)
            RETURN count(i) as total_incidents,
            collect(distinct i.type) as incident_types,
            collect(distinct i.sector) as sectors,
            collect(distinct i.location) as locations
        """)
        data = result.single()
        return {
            "total_incidents": data["total_incidents"],
            "incident_types": data["incident_types"],
            "sectors": data["sectors"],
            "locations": data["locations"]
        }

@app.get("/dashboard/chart")
async def get_chart_data():
    with driver.session() as session:
        result = session.run("""
            MATCH (i:Incident)
            WHERE i.timestamp >= datetime() - duration('P1D')
            RETURN i.timestamp as time, count(i) as count
            ORDER BY time
        """)
        data = [dict(record) for record in result]
        return {
            "labels": [d["time"] for d in data],
            "datasets": [{
                "label": "Incidents",
                "data": [d["count"] for d in data]
            }]
        }

@app.get("/incidents/recent")
async def get_recent_incidents():
    with driver.session() as session:
        result = session.run("""
            MATCH (i:Incident)
            RETURN i
            ORDER BY i.timestamp DESC
            LIMIT 10
        """)
        return [dict(record["i"]) for record in result]

@app.post("/incidents")
async def create_incident(incident: Incident):
    with driver.session() as session:
        result = session.run("""
            CREATE (i:Incident {
                title: $title,
                severity: $severity,
                sector: $sector,
                description: $description,
                timestamp: $timestamp
            })
            RETURN i
        """, incident.dict())
        return dict(result.single()["i"])

@app.get("/alerts")
async def get_alerts():
    with driver.session() as session:
        result = session.run("""
            MATCH (a:Alert)
            RETURN a
            ORDER BY a.timestamp DESC
            LIMIT 5
        """)
        return [dict(record["a"]) for record in result]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5001)
