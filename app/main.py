from fastapi import FastAPI
from app.routes.category import router as category_router

app = FastAPI()

app.include_router(category_router)

@app.get('/health-check')
def health_check():
    return True