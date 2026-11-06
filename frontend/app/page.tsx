"use client";
import { useEffect, useState } from "react";
import { handleTodoItems } from "./hooks";
import "./styles.scss";
import Item from "./todo-item";

export default function Home() {

  const { addItem, items, fetchItems } = handleTodoItems()

  const [todoName, setTodoName] = useState("")

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    await addItem(todoName);
  };


  useEffect(() => {
    fetchItems()
  }, [])

  console.log(JSON.stringify(items, null, 2))
  return (
    <main >
      <h1>Hallo Welt!</h1>
      <form className="create-container" onSubmit={(e) => handleSubmit(e)}>
        <label htmlFor="todo-input">Dein Plan:</label>
        <input
          type="text"
          id="todo-input"
          value={todoName}
          onChange={(e) => setTodoName(e.target.value)}
        />
        <button type="submit">Hinzufügen</button>
      </form>

      {items.map((item) => (
        <p key={item.id}>{item.name}</p>
      ))}

      

    </main>
  );
}
