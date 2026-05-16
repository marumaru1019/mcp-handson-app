import type { Todo, TodoCreate, TodoUpdate } from "../types/todo";

const API_BASE_URL = import.meta.env.VITE_API_URL || "";

async function request<T>(path: string, options?: RequestInit): Promise<T> {
  const response = await fetch(`${API_BASE_URL}${path}`, {
    headers: {
      "Content-Type": "application/json",
    },
    ...options,
  });

  if (!response.ok) {
    const error = await response.json().catch(() => ({ detail: "Unknown error" }));
    throw new Error(error.detail || `HTTP ${response.status}`);
  }

  return response.json();
}

export async function listTodos(): Promise<Todo[]> {
  return request<Todo[]>("/todos");
}

export async function getTodo(id: number): Promise<Todo> {
  return request<Todo>(`/todos/${id}`);
}

export async function createTodo(todo: TodoCreate): Promise<Todo> {
  return request<Todo>("/todos", {
    method: "POST",
    body: JSON.stringify(todo),
  });
}

export async function updateTodo(id: number, todo: TodoUpdate): Promise<Todo> {
  return request<Todo>(`/todos/${id}`, {
    method: "PUT",
    body: JSON.stringify(todo),
  });
}

export async function deleteTodo(id: number): Promise<Todo> {
  return request<Todo>(`/todos/${id}`, {
    method: "DELETE",
  });
}
