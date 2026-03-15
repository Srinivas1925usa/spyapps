from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field, field_validator
from typing import List

class DefaultSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
        frozen=True,
        env_nested_delimiter="__",
    )

class Settings(BaseSettings):
    """Application settings"""
    app_version: str = "1.0.0"
    debug: bool = True
    environment: str = "development"
    service_name: str = "rag-api"

    postgres_database_url: str = "postgresql://rag_user:rag_password@localhost:5432/rag_db"
    postgres_echo_sql: bool = False
    postgres_pool_size: int = 20
    postgres_max_overflow: int = 0

def get_settings() -> Settings:
    """Get Application settings """
    return Settings()