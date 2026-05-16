# todo-mcp

④ TODO API を呼び出す MCP サーバー で使う雛形です。

## セットアップ

```bash
cd handson-app/todo-mcp
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## 起動（ローカル）

別ターミナルで TODO API（ポート 8000）を起動した状態で:

```bash
python server.py
```

MCP サーバーは `http://0.0.0.0:8080/mcp` で待ち受けます。

## 環境変数

| 変数 | 既定値 | 説明 |
| :--- | :--- | :--- |
| `TODO_API_URL` | `http://localhost:8000` | 呼び出し先 TODO API のベース URL |
| `TODO_API_TIMEOUT` | `10` | HTTP タイムアウト（秒） |
| `MCP_HOST` | `0.0.0.0` | MCP サーバーがバインドするホスト |
| `MCP_PORT` | `8080` | MCP サーバーがバインドするポート |

## MCP Inspector での確認

```bash
npx @modelcontextprotocol/inspector
```

接続先 URL: `http://127.0.0.1:8080/mcp` （Transport Type: `Streamable HTTP`）
