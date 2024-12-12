from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from neo4j import GraphDatabase
from typing import List, Dict

app = FastAPI()

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

# Neo4j connection
URI = "neo4j://localhost:7687"
AUTH = ("neo4j", "CPAT5OChnHp6cXhaHmyzitohnQsGh6ucx4b7b13jwck")  # Replace with your credentials
DATABASE = "incident"

def get_db():
    return GraphDatabase.driver(URI, auth=AUTH, database=DATABASE)

@app.get("/api/news")
async def get_news():
    with get_db().session() as session:
        result = session.run("""
            MATCH (n:News)
            RETURN {
                id: n.id,
                title: n.title,
                description: n.description,
                image: n.image,
                type: n.type,
                impact: n.impact,
                location: n.location
            } as news
            ORDER BY n.timestamp DESC
        """)
        return [dict(record["news"]) for record in result]

@app.get("/api/attack-types")
async def get_attack_types():
    with get_db().session() as session:
        result = session.run("""
            MATCH (a:AttackType)
            RETURN DISTINCT a.name
            ORDER BY a.name
        """)
        return [record["a.name"] for record in result]

@app.get("/api/impact-levels")
async def get_impact_levels():
    with get_db().session() as session:
        result = session.run("""
            MATCH (i:Impact)
            RETURN DISTINCT i.level
            ORDER BY i.level
        """)
        return [record["i.level"] for record in result]

@app.get("/api/locations")
async def get_locations():
    with get_db().session() as session:
        result = session.run("""
            MATCH (l:Location)
            RETURN DISTINCT l.name
            ORDER BY l.name
        """)
        return [record["l.name"] for record in result]

@app.get("/api/current-stats")
async def get_current_stats():
    with get_db().session() as session:
        # Get active threats count
        active_threats = session.run("""
            MATCH (t:Threat)
            WHERE t.status = 'active'
            RETURN count(t) as count
        """).single()["count"]

        # Get resolved incidents count
        resolved_incidents = session.run("""
            MATCH (i:Incident)
            WHERE i.status = 'resolved'
            RETURN count(i) as count
        """).single()["count"]

        # Get pending alerts count
        pending_alerts = session.run("""
            MATCH (a:Alert)
            WHERE a.status = 'pending'
            RETURN count(a) as count
        """).single()["count"]

        # Get total related incidents
        related_incidents = session.run("""
            MATCH (i:Incident)
            RETURN count(i) as count
        """).single()["count"]

        return {
            "Active Threats": active_threats,
            "Resolved Incidents": resolved_incidents,
            "Pending Alerts": pending_alerts,
            "relatedIncidents": related_incidents
        }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5001)
