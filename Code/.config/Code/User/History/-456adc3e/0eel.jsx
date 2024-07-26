import React from "react";
import TodoCard from "./TodoCard";

export default function TodoList(props) {
  const { todos, deleteTodo } = props;

  return (
    <ul className="main">
      {todos.map((todo, index) => {
        return (
          <TodoCard key={index} {...props}>
            <p>{todo}</p>
          </TodoCard>
        );
      })}
    </ul>
  );
}
