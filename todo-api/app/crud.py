"""CRUD 操作."""

from datetime import datetime, timezone

from sqlalchemy.orm import Session

from . import models, schemas


def get_todos(
    db: Session, skip: int = 0, limit: int = 100
) -> list[models.Todo]:
    """TODO 一覧を取得する."""
    return db.query(models.Todo).offset(skip).limit(limit).all()


def get_todo(db: Session, todo_id: int) -> models.Todo | None:
    """指定した ID の TODO を取得する."""
    return db.query(models.Todo).filter(models.Todo.id == todo_id).first()


def create_todo(db: Session, todo: schemas.TodoCreate) -> models.Todo:
    """TODO を新規作成する."""
    db_todo = models.Todo(
        title=todo.title,
        description=todo.description,
    )
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo


def update_todo(
    db: Session, todo_id: int, todo: schemas.TodoUpdate
) -> models.Todo | None:
    """指定した ID の TODO を更新する."""
    db_todo = get_todo(db, todo_id)
    if db_todo is None:
        return None

    update_data = todo.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_todo, key, value)

    db_todo.updated_at = datetime.now(timezone.utc)
    db.commit()
    db.refresh(db_todo)
    return db_todo


def delete_todo(db: Session, todo_id: int) -> models.Todo | None:
    """指定した ID の TODO を削除する."""
    db_todo = get_todo(db, todo_id)
    if db_todo is None:
        return None

    db.delete(db_todo)
    db.commit()
    return db_todo
