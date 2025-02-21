from fastapi import FastAPI
from app.api.endpoints import monitoring

app = FastAPI(
    title="Gamiroo Monitoring Service",
    version="1.0",
    description="Provides endpoints to query system metrics and retrieve historical performance data."
)

# Include monitoring routes under the '/api/v1/monitoring' prefix.
app.include_router(monitoring.router, prefix="/api/v1/monitoring")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8001, reload=True)
