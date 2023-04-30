from fastapi import APIRouter
from app.api import endpoints
from app.api import dependencies

router = APIRouter()

router.include_router(endpoints.router)
