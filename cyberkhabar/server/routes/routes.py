from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/api/data")
async def get_data():
    # Replace with your data fetching logic
    data = {"message": "Hello, World!"}
    return JSONResponse(content=data)

@app.post("/api/data")
async def post_data(request: Request):
    # Replace with your data processing logic
    data = await request.json()
    response = {"received": data}
    return JSONResponse(content=response, status_code=201)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)