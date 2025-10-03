from pydantic import BaseModel


class VacancyBase(BaseModel):
    title: str
    description: str | None = None
    status: str = "open"


class VacancyCreate(VacancyBase):
    owner_id: int


class VacancyUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    status: str | None = None


class VacancyPublic(VacancyBase):
    id: int
    owner_id: int

    class Config:
        from_attributes = True


