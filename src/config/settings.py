import os
from pathlib import Path
from dotenv import load_dotenv
from pydantic import BaseModel, PositiveInt
from pydantic_settings import BaseSettings, SettingsConfigDict


BASE_DIR = Path(__file__).parent.parent.parent 
env_file = f"{BASE_DIR}/.env"

class EnvSettings(BaseSettings):
    API_ID: int
    API_HASH: str
    AI_API_KEY: str 

    model_config = SettingsConfigDict(env_file=env_file)


class Settings(BaseSettings):
    env: EnvSettings = EnvSettings()

settings = Settings() 


