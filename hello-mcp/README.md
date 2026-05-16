# hello-mcp

③ はじめての MCP サーバー で使う最小 MCP サーバーの雛形です。

## セットアップ

```bash
cd handson-app/hello-mcp
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## 起動

```bash
python server.py
```

デフォルトでは `http://127.0.0.1:8000/mcp` で待ち受けます。
TODO API（同じ 8000 番）と同時起動する場合は、`FastMCP("HelloMCP", port=8001)` のように
ポートを変更してください。

## MCP Inspector での確認

```bash
npx @modelcontextprotocol/inspector
```

接続先 URL: `http://127.0.0.1:8000/mcp` （Transport Type: `Streamable HTTP`）
