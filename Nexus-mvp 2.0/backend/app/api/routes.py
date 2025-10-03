from fastapi import APIRouter
from app.api import auth, hh, gemini, vacancies, candidates

router = APIRouter()


@router.get("/health")
def health() -> dict:
    return {"status": "ok"}

router.include_router(auth.router)
router.include_router(hh.router)
router.include_router(gemini.router)
router.include_router(vacancies.router)
router.include_router(candidates.router)


