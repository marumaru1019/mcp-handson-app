"""FastAPI アプリケーションのエントリーポイント."""

import os
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .database import Base, engine
from .routers import todos


@asynccontextmanager
async def lifespan(app: FastAPI):
    """アプリケーション起動時にテーブルを作成する."""
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(
    title="TODO管理API",
    description=(
        "TODO管理のためのREST APIです。"
        "Azure API ManagementからMCP Serverとして公開し、"
        "AIエージェントからTODO操作が可能になります。"
    ),
    version="1.0.0",
    lifespan=lifespan,
)

# CORS設定: 許可するオリジンを環境変数から取得（カンマ区切り）
allowed_origins = os.getenv("ALLOWED_ORIGINS", "http://localhost:5173").split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(todos.router)


@app.get(
    "/health",
    summary="ヘルスチェック",
    description="APIの稼働状態を確認します。",
    operation_id="health_check",
)
def health_check():
    """ヘルスチェックエンドポイント."""
    return {"status": "healthy"}
