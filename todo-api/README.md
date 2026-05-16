# todo-api

② TODO アプリの構成を理解する で使う FastAPI 製の TODO REST API（完成済み）です。
ハンズオン中は中身を編集する必要はありません。

## セットアップと起動

```bash
cd handson-app/todo-api
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

Swagger UI: <http://127.0.0.1:8000/docs>

## 主要エンドポイント

| メソッド | パス | 用途 |
| :--- | :--- | :--- |
| GET | `/health` | ヘルスチェック |
| GET | `/todos` | TODO 一覧 |
| GET | `/todos/{todo_id}` | TODO 詳細 |
| POST | `/todos` | TODO 作成 |
| PUT | `/todos/{todo_id}` | TODO 更新 |
| DELETE | `/todos/{todo_id}` | TODO 削除 |

データは SQLite (`todo.db`) に保存されます。初期化したい場合はサーバー停止後にファイルを削除してください。
