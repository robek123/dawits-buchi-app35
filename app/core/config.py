from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = 'DAWITS-BUCHI-APP35'

    class Config:
        env_file = '.env'


def get_settings():
    return Settings()
