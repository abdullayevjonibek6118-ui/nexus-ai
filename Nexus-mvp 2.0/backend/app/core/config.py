from pydantic import BaseModel
import os


class Settings(BaseModel):
    database_url: str = os.getenv(
        "DATABASE_URL", "postgresql+psycopg2://nexus:nexus@localhost:5432/nexus"
    )
    secret_key: str = os.getenv("SECRET_KEY", "change-me-in-prod")
    access_token_expires_minutes: int = int(os.getenv("ACCESS_EXPIRES_MIN", "30"))
    refresh_token_expires_days: int = int(os.getenv("REFRESH_EXPIRES_DAYS", "7"))

    # HH.ru OAuth
    hh_client_id: str | None = os.getenv("HH_CLIENT_ID")
    hh_client_secret: str | None = os.getenv("HH_CLIENT_SECRET")
    hh_redirect_uri: str | None = os.getenv("HH_REDIRECT_URI")
    hh_user_agent: str = os.getenv("HH_USER_AGENT", "NexusAI/1.0")

    # Gemini
    gemini_api_key: str | None = os.getenv("GEMINI_API_KEY")
    gemini_model: str = os.getenv("GEMINI_MODEL", "gemini-1.5-flash")


settings = Settings()


