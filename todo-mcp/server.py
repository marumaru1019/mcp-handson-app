"""TODO MCP サーバー（雛形 / Streamable HTTP transport）.

④ TODO API を呼び出す MCP サーバー のステップで使用します。
環境変数の読み込み・FastMCP の初期化・共通 HTTP クライアントまでは実装済みです。
ドキュメントの手順に従って、下の TODO 部分に 5 つの MCP ツールを実装してください。

実装するツール:
  - list_todos   : GET    /todos
  - get_todo     : GET    /todos/{id}
  - create_todo  : POST   /todos
  - update_todo  : PUT    /todos/{id}
  - delete_todo  : DELETE /todos/{id}
"""

from __future__ import annotations

import os
from typing import Any

import httpx
from mcp.server.fastmcp import FastMCP

# 既存 TODO API のベース URL（環境変数で切り替え可能）
TODO_API_URL = os.environ.get("TODO_API_URL", "http://localhost:8000").rstrip("/")
HTTP_TIMEOUT = float(os.environ.get("TODO_API_TIMEOUT", "10"))

# ホスト/ポート（Container Apps では 0.0.0.0:8080）
MCP_HOST = os.environ.get("MCP_HOST", "0.0.0.0")
MCP_PORT = int(os.environ.get("MCP_PORT", "8080"))

mcp = FastMCP(
    name="todo-mcp-server",
    host=MCP_HOST,
    port=MCP_PORT,
    # /mcp で Streamable HTTP を提供
    streamable_http_path="/mcp",
)


def _client() -> httpx.AsyncClient:
    """共通の HTTP クライアントを返す."""
    return httpx.AsyncClient(base_url=TODO_API_URL, timeout=HTTP_TIMEOUT)


# TODO(step4.2): list_todos / get_todo ツールを実装してください。
#   - @mcp.tool(name=..., description=...) を付与
#   - async with _client() as client: で TODO API を呼び出す
#   - resp.raise_for_status() でエラーを伝搬し、resp.json() を返す


# TODO(step4.3): create_todo ツールを実装してください。
#   - 引数: title: str, description: str = ""
#   - POST /todos に {"title": ..., "description": ...} を送る


# TODO(step4.4): update_todo / delete_todo ツールを実装してください。
#   - update_todo: 引数 (todo_id, title, description, is_completed) を PUT /todos/{id}
#   - delete_todo: DELETE /todos/{id}


if __name__ == "__main__":
    # Streamable HTTP transport で起動
    mcp.run(transport="streamable-http")
