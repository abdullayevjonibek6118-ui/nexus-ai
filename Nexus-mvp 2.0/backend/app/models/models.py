from sqlalchemy import Column, Integer, String, ForeignKey, Text, JSON
from sqlalchemy.orm import relationship
from app.db.base import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    role = Column(String(50), nullable=False, default="hr")
    balance_tokens = Column(Integer, nullable=False, default=0)

    vacancies = relationship("Vacancy", back_populates="owner")


class Vacancy(Base):
    __tablename__ = "vacancies"
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    status = Column(String(50), nullable=False, default="open")

    owner = relationship("User", back_populates="vacancies")
    candidates = relationship("Candidate", back_populates="vacancy")


class Candidate(Base):
    __tablename__ = "candidates"
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=True)
    skills = Column(Text, nullable=True)
    experience = Column(Text, nullable=True)
    resume_url = Column(String(512), nullable=True)
    vacancy_id = Column(Integer, ForeignKey("vacancies.id"), nullable=True)

    vacancy = relationship("Vacancy", back_populates="candidates")
    interview = relationship("Interview", back_populates="candidate", uselist=False)


class Interview(Base):
    __tablename__ = "interviews"
    id = Column(Integer, primary_key=True)
    candidate_id = Column(Integer, ForeignKey("candidates.id"), nullable=False)
    video_url = Column(String(512), nullable=True)
    analysis_json = Column(JSON, nullable=True)

    candidate = relationship("Candidate", back_populates="interview")


class AIRequest(Base):
    __tablename__ = "ai_requests"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    type = Column(String(50), nullable=False)
    tokens_used = Column(Integer, nullable=False, default=0)
    timestamp = Column(String(64), nullable=False)


class Transaction(Base):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    amount = Column(Integer, nullable=False)
    provider = Column(String(50), nullable=False)
    status = Column(String(50), nullable=False)


class Feedback(Base):
    __tablename__ = "feedback"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    message = Column(Text, nullable=True)
    rating = Column(Integer, nullable=True)


