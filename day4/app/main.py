from fastapi import FastAPI
from app.routers.stats import router as stats_router
from app.routers.files import router as files_router 
from app.routers.products import router as products_router


app = FastAPI(title="Day 4 APIs")
app.include_router(products_router)
app.include_router(stats_router)
app.include_router(files_router) 

@app.get("/")
def root():
    return {"message": "API running"}
