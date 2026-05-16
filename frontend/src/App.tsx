import { useCallback, useEffect, useState } from "react";
import { TodoForm } from "./components/TodoForm";
import { TodoList } from "./components/TodoList";
import * as api from "./api/todos";
import type { Todo, TodoCreate } from "./types/todo";
import "./App.css";

function App() {
  const [todos, setTodos] = useState<Todo[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  const fetchTodos = useCallback(async () => {
    try {
      setError(null);
      const data = await api.listTodos();
      setTodos(data);
    } catch (err) {
      setError(err instanceof Error ? err.message : "データの取得に失敗しました");
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => {
    fetchTodos();
  }, [fetchTodos]);

  const handleAdd = async (todo: TodoCreate) => {
    try {
      setError(null);
      const created = await api.createTodo(todo);
      setTodos((prev) => [...prev, created]);
    } catch (err) {
      setError(err instanceof Error ? err.message : "作成に失敗しました");
    }
  };

  const handleToggle = async (id: number, is_completed: boolean) => {
    try {
      setError(null);
      const updated = await api.updateTodo(id, { is_completed });
      setTodos((prev) => prev.map((t) => (t.id === id ? updated : t)));
    } catch (err) {
      setError(err instanceof Error ? err.message : "更新に失敗しました");
    }
  };

  const handleDelete = async (id: number) => {
    try {
      setError(null);
      await api.deleteTodo(id);
      setTodos((prev) => prev.filter((t) => t.id !== id));
    } catch (err) {
      setError(err instanceof Error ? err.message : "削除に失敗しました");
    }
  };

  return (
    <div className="app">
      <header>
        <h1>📝 TODO管理</h1>
      </header>
      <main>
        <TodoForm onAdd={handleAdd} />
        {error && <p className="error-message">{error}</p>}
        {loading ? (
          <p className="loading">読み込み中...</p>
        ) : (
          <TodoList
            todos={todos}
            onToggle={handleToggle}
            onDelete={handleDelete}
          />
        )}
      </main>
    </div>
  );
}

export default App;
