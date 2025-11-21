# Nexus AI (MVP)
Основатели:
Абдуллаев Жонибек
Акрамов Далер
Наги Халед Наги Ибрагим Эль-Шаркави
Интеллектуальная SaaS-платформа для автоматизации сорсинга, скрининга и подбора кандидатов с помощью ИИ.

## Стек
- Frontend: Next.js 14, TypeScript, Tailwind, ShadCN, Zustand
- Backend: FastAPI, SQLAlchemy, Alembic, Redis, Celery, RabbitMQ
- DB: PostgreSQL, Storage: S3
- AI: Gemini API (через backend proxy)

## Локальный запуск
```bash
# 1) Запуск базовых сервисов
docker compose up -d postgres redis rabbitmq

# 2) Backend (после scaffold)
cd backend
python -m venv .venv && .venv/Scripts/activate
pip install -r requirements.txt
uvicorn app.main:app --reload

# 3) Frontend (после scaffold)
cd frontend
pnpm install
pnpm dev
```

## Лицензия
Proprietary


