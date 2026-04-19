from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Nyx Voice Assistant API"
    environment: str = "development"
    database_url: str = "sqlite:///./nyx_voice_assistant.db"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()
