from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from neo4j import GraphDatabase
from typing import List, Dict
from pydantic import BaseModel

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
URI = "neo4j://localhost:7687"
AUTH = ("neo4j", "your_password")

def get_db():
    return GraphDatabase.driver(URI, auth=AUTH)

@app.get("/api/news")
async def get_news() -> List[Dict]:
    with get_db().session() as session:
        result = session.run("""
            MATCH (n:News)
            RETURN n.id, n.title, n.description, n.image, n.type, n.impact, n.location
        """)
        news = [dict(record['n']) for record in result]
        return news

@app.get("/api/attack-types")
async def get_attack_types() -> List[str]:
    with get_db().session() as session:
        result = session.run("MATCH (a:AttackType) RETURN a.name")
        types = [record['a.name'] for record in result]
        return types

@app.get("/api/impact-levels")
async def get_impact_levels() -> List[str]:
    with get_db().session() as session:
        result = session.run("MATCH (i:ImpactLevel) RETURN i.name")
        levels = [record['i.name'] for record in result]
        return levels

@app.get("/api/locations")
async def get_locations() -> List[str]:
    with get_db().session() as session:
        result = session.run("MATCH (l:Location) RETURN l.name")
        locations = [record['l.name'] for record in result]
        return locations

@app.get("/api/current-stats")
async def get_current_stats() -> Dict:
    with get_db().session() as session:
        active_threats = session.run("MATCH (t:Threat {status: 'active'}) RETURN count(t)").single()[0]
        resolved = session.run("MATCH (i:Incident {status: 'resolved'}) RETURN count(i)").single()[0]
        pending = session.run("MATCH (a:Alert {status: 'pending'}) RETURN count(a)").single()[0]
        related = session.run("MATCH (i:Incident) RETURN count(i)").single()[0]
        
        return {
            'Active Threats': active_threats,
            'Resolved Incidents': resolved,
            'Pending Alerts': pending,
            'relatedIncidents': related
        }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5001)