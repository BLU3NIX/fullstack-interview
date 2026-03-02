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
        try {
            const results = await fetch(`${BACKEND_URL}/todos/read`, {
                headers: {
                    "Content-Type": "application/json",
                },
            })
            const data = await results.json()
            setItems(data)
        } catch (error) {
            console.error("Error fetching ToDo items:", error)
        }
    }


    const addItem = async (name: string) => {
        const newItem: Omit<TodoItem, "id"> = {
            name,
            order: items ? items.length : 0,
            completed: false
        }
        try {
            await fetch(`${BACKEND_URL}/todos/create`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(newItem),
            })
            await fetchItems()
        } catch (error) {
            console.error("Error adding ToDo item:", error)
        }
    }


    const deleteItem = async (id: number) => {
        const item = items.find(i => i.id === id)
        if (!item) return
        try {
            await fetch(`${BACKEND_URL}/todos/delete/${id}`, {
                method: "DELETE",
                headers: {
                    "Content-Type": "application/json",
                },
            })
            await fetchItems()
        } catch (error) {
            console.error("Error adding ToDo item:", error)
        }
    }


    const toggleItem = async (id: number) => {
        const item = items.find(i => i.id === id)
        if (!item) return
        try {
            await fetch(`${BACKEND_URL}/todos/update/${id}`, {
                method: "PATCH",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ completed: !item.completed }),
            })
            await fetchItems()
        } catch (error) {
            console.error("Error editing ToDo item:", error)
        }
    }

    return {
        items,
        fetchItems,
        addItem,
        deleteItem,
        toggleItem
    }
}
