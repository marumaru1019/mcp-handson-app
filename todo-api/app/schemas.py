"""リクエスト/レスポンスの Pydantic スキーマ定義."""

from datetime import datetime

from pydantic import BaseModel, Field


class TodoCreate(BaseModel):
    """TODO 新規作成リクエストスキーマ."""

    title: str = Field(
        ..., min_length=1, max_length=255, description="TODOのタイトル"
    )
    description: str | None = Field(
        default=None, description="TODOの詳細説明"
    )


class TodoUpdate(BaseModel):
    """TODO 更新リクエストスキーマ."""

    title: str | None = Field(
        default=None, min_length=1, max_length=255, description="TODOのタイトル"
    )
    description: str | None = Field(
        default=None, description="TODOの詳細説明"
    )
    is_completed: bool | None = Field(
        default=None, description="完了フラグ"
    )


class TodoResponse(BaseModel):
    """TODO レスポンススキーマ."""

    id: int = Field(description="TODOのID")
    title: str = Field(description="TODOのタイトル")
    description: str | None = Field(description="TODOの詳細説明")
    is_completed: bool = Field(description="完了フラグ")
    created_at: datetime = Field(description="作成日時")
    updated_at: datetime = Field(description="更新日時")

    model_config = {"from_attributes": True}
