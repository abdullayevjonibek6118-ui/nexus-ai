from pydantic import BaseModel, EmailStr


class CandidateBase(BaseModel):
    name: str
    email: EmailStr | None = None
    skills: str | None = None
    experience: str | None = None
    resume_url: str | None = None
    vacancy_id: int | None = None


class CandidateCreate(CandidateBase):
    name: str


class CandidateUpdate(BaseModel):
    name: str | None = None
    email: EmailStr | None = None
    skills: str | None = None
    experience: str | None = None
    resume_url: str | None = None
    vacancy_id: int | None = None


class CandidatePublic(CandidateBase):
    id: int

    class Config:
        from_attributes = True


