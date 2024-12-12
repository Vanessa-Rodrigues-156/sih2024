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

# Neo4j connection
URI = "neo4j://localhost:7687"
AUTH = ("neo4j", "CPAT5OChnHp6cXhaHmyzitohnQsGh6ucx4b7b13jwck")  # Replace with your credentials
DATABASE = "incident"

def get_db():
    return GraphDatabase.driver(URI, auth=AUTH, database=DATABASE)

# Models
class Incident(BaseModel):
    id: str
    title: str
    description: str
    date: datetime

class Threat(BaseModel):
    id: str
    name: str
    description: str

class Report(BaseModel):
    id: str
    title: str
    content: str
    timestamp: datetime

class Alert(BaseModel):
    id: str
    message: str
    date: datetime

class Location(BaseModel):
    location: str

class CurrentStats(BaseModel):
    active_threats: int
    resolved_incidents: int
    pending_alerts: int
    related_incidents: int

class User(BaseModel):
    username: str
    password: str

class NewsHeadline(BaseModel):
    id: str
    title: str
    content: str
    date: str

# Routes
@app.get("/api/incidents", response_model=List[Incident])
async def get_incidents():
    with get_db().session() as session:
        result = session.run("""
            MATCH (i:Incident)
            RETURN i.id as id, i.title as title, i.description as description, i.date as date
        """)
        incidents = [Incident(id=record["id"], title=record["title"], description=record["description"], date=record["date"]) for record in result]
        return incidents

@app.get("/api/threats", response_model=List[Threat])
async def get_threats():
    with get_db().session() as session:
        result = session.run("""
            MATCH (t:Threat)
            RETURN t.id as id, t.name as name, t.description as description
        """)
        threats = [Threat(id=record["id"], name=record["name"], description=record["description"]) for record in result]
        return threats

@app.get("/api/reports", response_model=List[Report])
async def get_reports():
    with get_db().session() as session:
        result = session.run("""
            MATCH (r:Report)
            RETURN r.id as id, r.title as title, r.content as content, r.timestamp as timestamp
        """)
        reports = [Report(id=record["id"], title=record["title"], content=record["content"], timestamp=record["timestamp"]) for record in result]
        return reports

@app.get("/api/alerts", response_model=List[Alert])
async def get_alerts():
    with get_db().session() as session:
        result = session.run("""
            MATCH (a:Alert)
            RETURN a.id as id, a.message as message, a.date as date
        """)
        alerts = [Alert(id=record["id"], message=record["message"], date=record["date"]) for record in result]
        return alerts

@app.get("/api/reports/{report_id}", response_model=Report)
async def get_report(report_id: str):
    with get_db().session() as session:
        result = session.run("""
            MATCH (r:Report {id: $id})
            RETURN r.id as id, r.title as title, r.content as content, r.timestamp as timestamp
        """, id=report_id)
        record = result.single()
        if record:
            return Report(
                id=record["id"],
                title=record["title"],
                content=record["content"],
                timestamp=datetime.fromisoformat(record["timestamp"])
            )
        else:
            raise HTTPException(status_code=404, detail="Report not found")

@app.get("/api/news", response_model=List[NewsHeadline])
async def get_news():
    with get_db().session() as session:
        result = session.run("""
            MATCH (n:News)
            RETURN n.id as id, n.title as title, n.content as content, n.date as date
        """)
        news = [NewsHeadline(id=record["id"], title=record["title"], content=record["content"], date=record["date"]) for record in result]
        return news

@app.get("/api/attack-types", response_model=List[str])
async def get_attack_types():
    with get_db().session() as session:
        result = session.run("""
            MATCH (a:AttackType)
            RETURN DISTINCT a.name
            ORDER BY a.name
        """)
        return [record["a.name"] for record in result]

@app.get("/api/impact-levels", response_model=List[str])
async def get_impact_levels():
    with get_db().session() as session:
        result = session.run("""
            MATCH (i:Impact)
            RETURN DISTINCT i.level
            ORDER BY i.level
        """)
        return [record["i.level"] for record in result]

@app.get("/api/locations", response_model=List[str])
async def get_locations():
    with get_db().session() as session:
        result = session.run("""
            MATCH (l:Location)
            RETURN DISTINCT l.name
            ORDER BY l.name
        """)
        return [record["l.name"] for record in result]

@app.get("/api/current-stats", response_model=CurrentStats)
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
            "active_threats": active_threats,
            "resolved_incidents": resolved_incidents,
            "pending_alerts": pending_alerts,
            "related_incidents": related_incidents
        }

@app.get("/dashboard/stats")
async def get_dashboard_stats():
    with get_db().session() as session:
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
    with get_db().session() as session:
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
    with get_db().session() as session:
        result = session.run("""
            MATCH (i:Incident)
            RETURN i
            ORDER BY i.timestamp DESC
            LIMIT 10
        """)
        return [dict(record["i"]) for record in result]

@app.post("/incidents")
async def create_incident(incident: Incident):
    with get_db().session() as session:
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

@app.post("/login")
async def login(user: User):
    with get_db().session() as session:
        result = session.run("""
            MATCH (u:User {username: $username, password: $password})
            RETURN u
        """, user.dict())
        user_data = result.single()
        if not user_data:
            raise HTTPException(status_code=401, detail="Invalid credentials")
        return dict(user_data["u"])

@app.get("/analytics")
async def get_analytics():
    with get_db().session() as session:
        result = session.run("""
            MATCH (i:Incident)
            RETURN i.sector as sector, count(i) as count
            ORDER BY count DESC
        """)
        return [dict(record) for record in result]

@app.get("/profile/{username}")
async def get_user_profile(username: str):
    with get_db().session() as session:
        result = session.run("""
            MATCH (u:User {username: $username})
            RETURN u
        """, {"username": username})
        user_data = result.single()
        if not user_data:
            raise HTTPException(status_code=404, detail="User not found")
        return dict(user_data["u"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5001)