import { useState } from "react"
import { CreateTodoResponse, DeleteTodoResponse, TodoItem, ToggleTodoResponse } from "./types"

const BACKEND_URL = "http://localhost:8000"

const SAMPLE_TODOS = [
    {
        id: 1,
        name: "Sample ToDo Item",
        order: 0,
        completed: false
    },
    {
        id: 2,
        name: "Another Sample ToDo Item",
        order: 1,
        completed: true
    },
    {
        id: 3,
        name: "Yet Another Sample ToDo Item",
        order: 2,
        completed: false
    }
]

export const handleTodoItems = () => {
    const [items, setItems] = useState<TodoItem[]>([])

    // TODOS
    const fetchItems = async () => {

    }

    const addItem = async (name: string) => {

    }

    const deleteItem = async (id: number) => {

    }

    const toggleItem = async (id: number) => {

    }

    return {

    }
}
