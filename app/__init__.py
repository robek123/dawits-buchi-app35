from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app import models
from app.api import router as api_router
from app.core import config
from app.core.database import Base, engine


def create_tables():
    Base.metadata.create_all(bind=engine)


def start_service() -> None:
    app = FastAPI(title=config.get_settings().app_name)
    create_tables()
    app.include_router(api_router)
    return app


app = start_service()


# Dependency

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
