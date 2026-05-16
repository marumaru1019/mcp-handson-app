"""TODO エンドポイント定義."""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..crud import create_todo, delete_todo, get_todo, get_todos, update_todo
from ..database import get_db
from ..schemas import TodoCreate, TodoResponse, TodoUpdate

router = APIRouter(prefix="/todos", tags=["todos"])


@router.get(
    "",
    response_model=list[TodoResponse],
    summary="TODO一覧を取得する",
    description="登録されているTODOの一覧を取得します。skip と limit で取得範囲を指定できます。",
    operation_id="list_todos",
)
def list_todos(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
) -> list[TodoResponse]:
    """TODO 一覧を取得する."""
    todos = get_todos(db, skip=skip, limit=limit)
    return todos


@router.get(
    "/{todo_id}",
    response_model=TodoResponse,
    summary="TODOの詳細を取得する",
    description="指定したIDのTODOの詳細情報を取得します。",
    operation_id="get_todo",
)
def read_todo(
    todo_id: int, db: Session = Depends(get_db)
) -> TodoResponse:
    """指定した ID の TODO を取得する."""
    todo = get_todo(db, todo_id)
    if todo is None:
        raise HTTPException(status_code=404, detail="TODO not found")
    return todo


@router.post(
    "",
    response_model=TodoResponse,
    status_code=201,
    summary="新しいTODOを作成する",
    description="タイトルと任意の説明を指定して新しいTODOを作成します。",
    operation_id="create_todo",
)
def create(
    todo: TodoCreate, db: Session = Depends(get_db)
) -> TodoResponse:
    """TODO を新規作成する."""
    return create_todo(db, todo)


@router.put(
    "/{todo_id}",
    response_model=TodoResponse,
    summary="TODOを更新する",
    description="指定したIDのTODOのタイトル、説明、完了フラグを更新します。",
    operation_id="update_todo",
)
def update(
    todo_id: int, todo: TodoUpdate, db: Session = Depends(get_db)
) -> TodoResponse:
    """指定した ID の TODO を更新する."""
    updated = update_todo(db, todo_id, todo)
    if updated is None:
        raise HTTPException(status_code=404, detail="TODO not found")
    return updated


@router.delete(
    "/{todo_id}",
    response_model=TodoResponse,
    summary="TODOを削除する",
    description="指定したIDのTODOを削除します。",
    operation_id="delete_todo",
)
def delete(
    todo_id: int, db: Session = Depends(get_db)
) -> TodoResponse:
    """指定した ID の TODO を削除する."""
    deleted = delete_todo(db, todo_id)
    if deleted is None:
        raise HTTPException(status_code=404, detail="TODO not found")
    return deleted
