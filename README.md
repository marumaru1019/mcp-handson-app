# handson-app

MCP ハンズオン参加者用のスターターディレクトリです。

## ディレクトリ構成

| パス | 章 | 役割 |
| :--- | :--- | :--- |
| `todo-api/` | ② TODO アプリ起動 | FastAPI 製の TODO REST API（完成済み・触らない） |
| `frontend/` | ② 任意 | React + Vite 製の TODO 管理画面（完成済み） |
| `hello-mcp/` | ③ はじめての MCP サーバー | 最小 MCP サーバーの**雛形**（参加者がツールを実装する） |
| `todo-mcp/` | ④ TODO API を呼び出す MCP サーバー | TODO API を呼ぶ MCP サーバーの**雛形**（参加者がツールを実装する） |
| `infra/` | ⑥ Azure Container Apps デプロイ | `azd` 用 Bicep |
| `azure.yaml` | ⑥ | `azd` のサービス定義（api / mcp / web） |

## 進め方

ドキュメント [docs/mcp-content/](../content/ja/docs/mcp-content/_index.md) の手順に従い、
以下の順に作業します。

1. `todo-api/` で TODO API をローカル起動（②）
2. `hello-mcp/` で最小 MCP サーバーを実装（③）
3. `todo-mcp/` で TODO API を呼ぶ MCP サーバーを実装（④）
4. `.vscode/mcp.json` を作って Copilot から接続（⑤）
5. `azd up` で Azure Container Apps にデプロイ（⑥）
