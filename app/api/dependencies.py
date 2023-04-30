from fastapi import Depends
from app.core.config import get_settings


def get_current_settings() -> settings.Settings:
    return get_settings()
