import type { Todo } from "../types/todo";

interface Props {
  todo: Todo;
  onToggle: (id: number, is_completed: boolean) => void;
  onDelete: (id: number) => void;
}

export function TodoItem({ todo, onToggle, onDelete }: Props) {
  return (
    <li className={`todo-item ${todo.is_completed ? "completed" : ""}`}>
      <div className="todo-content">
        <label className="todo-checkbox">
          <input
            type="checkbox"
            checked={todo.is_completed}
            onChange={() => onToggle(todo.id, !todo.is_completed)}
          />
          <span className="todo-title">{todo.title}</span>
        </label>
        {todo.description && (
          <p className="todo-description">{todo.description}</p>
        )}
        <span className="todo-date">
          {new Date(todo.created_at).toLocaleDateString("ja-JP")}
        </span>
      </div>
      <button
        className="delete-btn"
        onClick={() => onDelete(todo.id)}
        title="削除"
      >
        ✕
      </button>
    </li>
  );
}
