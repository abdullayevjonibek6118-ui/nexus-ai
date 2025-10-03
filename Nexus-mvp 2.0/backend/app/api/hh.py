from fastapi import APIRouter, HTTPException, Query
from urllib.parse import urlencode
import httpx
from app.core.config import settings


router = APIRouter(prefix="/hh", tags=["hh"])


@router.get("/oauth/url")
def get_oauth_url() -> dict:
    if not settings.hh_client_id or not settings.hh_redirect_uri:
        raise HTTPException(status_code=500, detail="HH OAuth is not configured")
    params = {
        "response_type": "code",
        "client_id": settings.hh_client_id,
        "redirect_uri": settings.hh_redirect_uri,
    }
    url = f"https://hh.ru/oauth/authorize?{urlencode(params)}"
    return {"auth_url": url}


@router.get("/oauth/callback")
async def oauth_callback(code: str = Query(...)) -> dict:
    if not all([settings.hh_client_id, settings.hh_client_secret, settings.hh_redirect_uri]):
        raise HTTPException(status_code=500, detail="HH OAuth is not configured")
    token_url = "https://hh.ru/oauth/token"
    data = {
        "grant_type": "authorization_code",
        "code": code,
        "client_id": settings.hh_client_id,
        "client_secret": settings.hh_client_secret,
        "redirect_uri": settings.hh_redirect_uri,
    }
    headers = {"User-Agent": settings.hh_user_agent}
    async with httpx.AsyncClient() as client:
        resp = await client.post(token_url, data=data, headers=headers)
        if resp.status_code != 200:
            raise HTTPException(status_code=resp.status_code, detail=resp.text)
        tokens = resp.json()
    return tokens


