from fastapi import FastAPI

from app import app


app = FastAPI()


@app.get('/')
async def root():
    return "Hello, World!"


app.include_router()
