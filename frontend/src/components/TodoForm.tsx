import { useState } from "react";
import type { TodoCreate } from "../types/todo";

interface Props {
  onAdd: (todo: TodoCreate) => void;
}

export function TodoForm({ onAdd }: Props) {
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!title.trim()) return;
    onAdd({
      title: title.trim(),
      description: description.trim() || null,
    });
    setTitle("");
    setDescription("");
  };

  return (
    <form onSubmit={handleSubmit} className="todo-form">
      <input
        type="text"
        placeholder="TODOのタイトル"
        value={title}
        onChange={(e) => setTitle(e.target.value)}
        required
        maxLength={255}
      />
      <input
        type="text"
        placeholder="説明（任意）"
        value={description}
        onChange={(e) => setDescription(e.target.value)}
      />
      <button type="submit">追加</button>
    </form>
  );
}
