import type { Todo } from "../types/todo";
import { TodoItem } from "./TodoItem";

interface Props {
  todos: Todo[];
  onToggle: (id: number, is_completed: boolean) => void;
  onDelete: (id: number) => void;
}

export function TodoList({ todos, onToggle, onDelete }: Props) {
  if (todos.length === 0) {
    return <p className="empty-message">TODOはまだありません。上のフォームから追加してください。</p>;
  }

  const pending = todos.filter((t) => !t.is_completed);
  const completed = todos.filter((t) => t.is_completed);

  return (
    <div>
      {pending.length > 0 && (
        <section>
          <h2>未完了 ({pending.length})</h2>
          <ul className="todo-list">
            {pending.map((todo) => (
              <TodoItem
                key={todo.id}
                todo={todo}
                onToggle={onToggle}
                onDelete={onDelete}
              />
            ))}
          </ul>
        </section>
      )}
      {completed.length > 0 && (
        <section>
          <h2>完了済み ({completed.length})</h2>
          <ul className="todo-list">
            {completed.map((todo) => (
              <TodoItem
                key={todo.id}
                todo={todo}
                onToggle={onToggle}
                onDelete={onDelete}
              />
            ))}
          </ul>
        </section>
      )}
    </div>
  );
}
