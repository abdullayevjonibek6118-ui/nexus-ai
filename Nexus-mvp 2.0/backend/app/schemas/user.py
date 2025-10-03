from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: EmailStr
    role: str = "hr"


class UserCreate(UserBase):
    password: str


class UserPublic(UserBase):
    id: int
    balance_tokens: int = 0

    class Config:
        from_attributes = True


class TokenPair(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"


