from app.db.base import Base, engine
from app.models import models  # noqa: F401 ensure models are imported


def init_db() -> None:
    Base.metadata.create_all(bind=engine)


