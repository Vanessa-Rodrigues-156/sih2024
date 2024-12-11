
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional, Dict, Any
import pandas as pd
import numpy as np
from datetime import datetime
import uvicorn
import json

app = FastAPI(title="Data Visualization API",
              description="API for handling and visualizing large datasets")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Data models
class DataPoint(BaseModel):
    timestamp: datetime
    value: float
    category: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None

class Dataset(BaseModel):
    name: str
    data: List[DataPoint]

# In-memory storage (replace with database in production)
datasets = {}

# Helper functions
def calculate_statistics(data: List[DataPoint]):
    values = [point.value for point in data]
    return {
        "count": len(values),
        "mean": np.mean(values),
        "median": np.median(values),
        "std": np.std(values),
        "min": min(values),
        "max": max(values)
    }

def create_time_series(data: List[DataPoint]):
    df = pd.DataFrame([{
        "timestamp": point.timestamp,
        "value": point.value,
        "category": point.category
    } for point in data])
    
    return df.groupby([
        pd.Grouper(key='timestamp', freq='1D'),
        'category'
    ])['value'].mean().unstack().to_dict()

# API Endpoints
@app.post("/dataset/")
async def create_dataset(dataset: Dataset):
    """Create a new dataset"""
    if dataset.name in datasets:
        raise HTTPException(status_code=400, detail="Dataset already exists")
    
    datasets[dataset.name] = dataset.data
    return {"message": f"Dataset '{dataset.name}' created successfully"}

@app.get("/dataset/{name}/statistics")
async def get_statistics(name: str):
    """Get basic statistics for a dataset"""
    if name not in datasets:
        raise HTTPException(status_code=404, detail="Dataset not found")
    
    return calculate_statistics(datasets[name])

@app.get("/dataset/{name}/timeseries")
async def get_timeseries(name: str, 
                        start_date: Optional[datetime] = None,
                        end_date: Optional[datetime] = None):
    """Get time series data for visualization"""
    if name not in datasets:
        raise HTTPException(status_code=404, detail="Dataset not found")
    
    data = datasets[name]
    
    # Filter by date range if provided
    if start_date:
        data = [d for d in data if d.timestamp >= start_date]
    if end_date:
        data = [d for d in data if d.timestamp <= end_date]
    
    return create_time_series(data)

@app.get("/dataset/{name}/histogram")
async def get_histogram(name: str, bins: int = 10):
    """Get histogram data for visualization"""
    if name not in datasets:
        raise HTTPException(status_code=404, detail="Dataset not found")
    
    values = [point.value for point in datasets[name]]
    hist, bin_edges = np.histogram(values, bins=bins)
    
    return {
        "counts": hist.tolist(),
        "bin_edges": bin_edges.tolist()
    }

@app.get("/dataset/{name}/categories")
async def get_categories(name: str):
    """Get data grouped by categories"""
    if name not in datasets:
        raise HTTPException(status_code=404, detail="Dataset not found")
    
    categories = {}
    for point in datasets[name]:
        if point.category:
            if point.category not in categories:
                categories[point.category] = []
            categories[point.category].append(point.value)
    
    return {
        category: {
            "count": len(values),
            "mean": np.mean(values),
            "sum": sum(values)
        }
        for category, values in categories.items()
    }

@app.delete("/dataset/{name}")
async def delete_dataset(name: str):
    """Delete a dataset"""
    if name not in datasets:
        raise HTTPException(status_code=404, detail="Dataset not found")
    
    del datasets[name]
    return {"message": f"Dataset '{name}' deleted successfully"}

if _name_ == "_main_":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)