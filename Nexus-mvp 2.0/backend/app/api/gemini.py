from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import httpx
from app.core.config import settings


router = APIRouter(prefix="/gemini", tags=["gemini"])


class TextRequest(BaseModel):
    prompt: str


@router.post("/text")
async def gemini_text(req: TextRequest) -> dict:
    if not settings.gemini_api_key:
        raise HTTPException(status_code=500, detail="Gemini API key not configured")

    # Simple proxy to Gemini Generative Language API (hypothetical endpoint)
    endpoint = f"https://generativelanguage.googleapis.com/v1beta/models/{settings.gemini_model}:generateContent?key={settings.gemini_api_key}"
    payload = {"contents": [{"parts": [{"text": req.prompt}]}]}

    async with httpx.AsyncClient(timeout=60) as client:
        resp = await client.post(endpoint, json=payload)
        if resp.status_code != 200:
            raise HTTPException(status_code=resp.status_code, detail=resp.text)
        data = resp.json()
    return data


