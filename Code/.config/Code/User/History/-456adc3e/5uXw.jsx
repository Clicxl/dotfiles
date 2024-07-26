import React from "react";
import TodoCard from "./TodoCard"

export default function TodoList() {
  let todos = ["Make Rice", "Cook"];
  return (
    <ul className="main">
      {todos.map((todo, index) => {
        return (
         <TodoCard key={index}>
          <p>{todo}</p>
         </TodoCard>
        );
      })}
    </ul>
  );
}
