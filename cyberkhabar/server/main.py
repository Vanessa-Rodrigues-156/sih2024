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

# Connect to Neo4j
driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "CPAT5OChnHp6cXhaHmyzitohnQsGh6ucx4b7b13jwck"))

try:
    driver.verify_connectivity()
    print("Successfully connected to the database.")
except Exception as e:
    print(f"Failed to connect to the database: {e}")

# Models

class Report(BaseModel):
    id: str
    title: str
    content: str
    timestamp: datetime

class NewsHeadline(BaseModel):
    id: str
    title: str
    content: str
    date: str

class AttackType(BaseModel):
    type: str

class ImpactLevel(BaseModel):
    level: str

class Location(BaseModel):
    location: str

class CurrentStats(BaseModel):
    active_threats: int
    resolved_incidents: int
    pending_alerts: int
    related_incidents: int

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

class User(BaseModel):
    username: str
    password: str

class Report(BaseModel):
    title: str
    content: str
    timestamp: datetime
class NewsHeadline(BaseModel):
    id: str
    title: str
    content: str
    date: str

# Routes
@app.get("/api/nodes/News", response_model=List[NewsHeadline])
async def get_news_headlines():
    with driver.session() as session:
        result = session.run("""
            MATCH (n:News)
            RETURN n.id as id, n.title as title, n.content as content, n.date as date
        """)
        news_headlines = [NewsHeadline(id=record["id"], title=record["title"], content=record["content"], date=record["date"]) for record in result]
        return news_headlines
@app.get("/api/news", response_model=List[NewsHeadline])
async def get_news_headlines():
    with driver.session() as session:
        result = session.run("""
            MATCH (n:News)
            RETURN n.id as id, n.title as title, n.content as content, n.date as date
        """)
        news_headlines = [NewsHeadline(id=record["id"], title=record["title"], content=record["content"], date=record["date"]) for record in result]
        return news_headlines

@app.get("/api/attack-types", response_model=List[AttackType])
async def get_attack_types():
    with driver.session() as session:
        result = session.run("""
            MATCH (a:AttackType)
            RETURN a.type as type
        """)
        attack_types = [AttackType(type=record["type"]) for record in result]
        return attack_types

@app.get("/api/impact-levels", response_model=List[ImpactLevel])
async def get_impact_levels():
    with driver.session() as session:
        result = session.run("""
            MATCH (i:ImpactLevel)
            RETURN i.level as level
        """)
        impact_levels = [ImpactLevel(level=record["level"]) for record in result]
        return impact_levels

@app.get("/api/locations", response_model=List[Location])
async def get_locations():
    with driver.session() as session:
        result = session.run("""
            MATCH (l:Location)
            RETURN l.location as location
        """)
        locations = [Location(location=record["location"]) for record in result]
        return locations

@app.get("/api/current-stats", response_model=CurrentStats)
async def get_current_stats():
    with driver.session() as session:
        result = session.run("""
            MATCH (s:Stats)
            RETURN s.active_threats as active_threats, s.resolved_incidents as resolved_incidents, s.pending_alerts as pending_alerts, s.related_incidents as related_incidents
        """)
        stats = result.single()
        if stats:
            return CurrentStats(
                active_threats=stats["active_threats"],
                resolved_incidents=stats["resolved_incidents"],
                pending_alerts=stats["pending_alerts"],
                related_incidents=stats["related_incidents"]
            )
        else:
            raise HTTPException(status_code=404, detail="Stats not found")

@app.get("/api/reports/{report_id}", response_model=Report)
async def get_report(report_id: str):
    with driver.session() as session:
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

@app.post("/login")
async def login(user: User):
    with driver.session() as session:
        result = session.run("""
            MATCH (u:User {username: $username, password: $password})
            RETURN u
        """, user.dict())
        user_data = result.single()
        if not user_data:
            raise HTTPException(status_code=401, detail="Invalid credentials")
        return dict(user_data["u"])

@app.get("/reports")
async def get_reports():
    with driver.session() as session:
        result = session.run("""
            MATCH (r:Report)
            RETURN r
            ORDER BY r.timestamp DESC
        """)
        return [dict(record["r"]) for record in result]

@app.post("/reports")
async def create_report(report: Report):
    with driver.session() as session:
        result = session.run("""
            CREATE (r:Report {
                title: $title,
                content: $content,
                timestamp: $timestamp
            })
            RETURN r
        """, report.dict())
        return dict(result.single()["r"])

@app.get("/analytics")
async def get_analytics():
    with driver.session() as session:
        result = session.run("""
            MATCH (i:Incident)
            RETURN i.sector as sector, count(i) as count
            ORDER BY count DESC
        """)
        return [dict(record) for record in result]

@app.get("/profile/{username}")
async def get_user_profile(username: str):
    with driver.session() as session:
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