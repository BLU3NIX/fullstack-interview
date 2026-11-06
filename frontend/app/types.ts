export type TodoItem = {
    id: number;
    name: string;
    order: number;
    completed: boolean;
}

export type CreateTodoResponse = {
    successful: boolean;
    created_todo: TodoItem;
    error: string;
}

export type ToggleTodoResponse = {
    successful: boolean;
    updatedTodo: TodoItem;
    error: string;
}

export type DeleteTodoResponse = {
    successful: boolean;
    deletedTodo: TodoItem;
    error: string;
}
