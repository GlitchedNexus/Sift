from fastapi import FastAPI

from api.health import router as health_router
from api.prediction import router as prediction_router

app = FastAPI(
    title="Sift",
    description="Backend service for geological deature extraction.",
)

app.include_router(prediction_router)
app.include_router(health_router)
