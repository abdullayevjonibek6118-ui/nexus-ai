from datetime import datetime, timedelta, timezone
import jwt
from fastapi import APIRouter, HTTPException
from passlib.context import CryptContext
from app.core.config import settings
from app.schemas.user import TokenPair, UserCreate


router = APIRouter(prefix="/auth", tags=["auth"])
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def _create_token(subject: str, expires_delta: timedelta) -> str:
    payload = {
        "sub": subject,
        "exp": datetime.now(timezone.utc) + expires_delta,
        "iat": datetime.now(timezone.utc),
    }
    return jwt.encode(payload, settings.secret_key, algorithm="HS256")


@router.post("/register", response_model=TokenPair)
def register(_: UserCreate) -> TokenPair:
    # Stub implementation: issue tokens without persistence
    access = _create_token("user:1", timedelta(minutes=settings.access_token_expires_minutes))
    refresh = _create_token("user:1", timedelta(days=settings.refresh_token_expires_days))
    return TokenPair(access_token=access, refresh_token=refresh)


@router.post("/login", response_model=TokenPair)
def login() -> TokenPair:
    access = _create_token("user:1", timedelta(minutes=settings.access_token_expires_minutes))
    refresh = _create_token("user:1", timedelta(days=settings.refresh_token_expires_days))
    return TokenPair(access_token=access, refresh_token=refresh)


