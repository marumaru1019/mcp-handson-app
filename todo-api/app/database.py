"""データベース接続・セッション管理."""

import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./todo.db")

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {},
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    """SQLAlchemy の宣言的ベースクラス."""

    pass


def get_db():
    """データベースセッションの依存性注入用ジェネレータ."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
