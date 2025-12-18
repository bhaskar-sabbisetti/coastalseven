from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="FastAPI MongoDB App")

app.include_router(router)
