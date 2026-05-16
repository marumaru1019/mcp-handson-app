"""はじめての MCP サーバー（雛形）.

この雛形は ③ はじめての MCP サーバー のステップで使用します。
`@mcp.tool()` を使って `add` 関数を MCP のツールとして登録してください。
ドキュメントの手順に従って、下の TODO 部分にコードを追加します。
"""

from mcp.server.fastmcp import FastMCP

# MCP サーバーのインスタンスを作成
mcp = FastMCP("HelloMCP")


# TODO(step3): 下に @mcp.tool() を使って add(a: int, b: int) -> int を実装してください。
#              docstring に「2 つの整数を加算して返す」と書くことで LLM が用途を理解できます。


if __name__ == "__main__":
    # Streamable HTTP transport で起動（既定ポート 8000）
    mcp.run(transport="streamable-http")
