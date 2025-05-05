from fastapi import FastAPI
from backend.routes import router

app = FastAPI(title="LangGraph PDF Classifier API")
app.include_router(router)
