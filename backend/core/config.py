from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    secret_key: str                
    algorithm: str = "HS256"                          
    access_token_expires_minutes: int = 30
    database_url: str = "sqlite:///./trace.db"

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()