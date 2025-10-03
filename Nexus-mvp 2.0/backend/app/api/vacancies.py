from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.session import get_db
from app.models.models import Vacancy
from app.schemas.vacancy import VacancyCreate, VacancyPublic, VacancyUpdate


router = APIRouter(prefix="/vacancies", tags=["vacancies"])


@router.post("/", response_model=VacancyPublic)
def create_vacancy(payload: VacancyCreate, db: Session = Depends(get_db)):
    vacancy = Vacancy(
        title=payload.title,
        description=payload.description,
        status=payload.status,
        owner_id=payload.owner_id,
    )
    db.add(vacancy)
    db.commit()
    db.refresh(vacancy)
    return vacancy


@router.get("/", response_model=List[VacancyPublic])
def list_vacancies(db: Session = Depends(get_db)):
    return db.query(Vacancy).all()


@router.get("/{vacancy_id}", response_model=VacancyPublic)
def get_vacancy(vacancy_id: int, db: Session = Depends(get_db)):
    vacancy = db.get(Vacancy, vacancy_id)
    if not vacancy:
        raise HTTPException(status_code=404, detail="Vacancy not found")
    return vacancy


@router.patch("/{vacancy_id}", response_model=VacancyPublic)
def update_vacancy(vacancy_id: int, payload: VacancyUpdate, db: Session = Depends(get_db)):
    vacancy = db.get(Vacancy, vacancy_id)
    if not vacancy:
        raise HTTPException(status_code=404, detail="Vacancy not found")
    for field, value in payload.model_dump(exclude_unset=True).items():
        setattr(vacancy, field, value)
    db.commit()
    db.refresh(vacancy)
    return vacancy


@router.delete("/{vacancy_id}")
def delete_vacancy(vacancy_id: int, db: Session = Depends(get_db)):
    vacancy = db.get(Vacancy, vacancy_id)
    if not vacancy:
        raise HTTPException(status_code=404, detail="Vacancy not found")
    db.delete(vacancy)
    db.commit()
    return {"ok": True}


