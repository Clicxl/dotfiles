import React, { useState } from "react";

export default function TodoInput(props) {
  const { addTodo } = props;
  const [todoValue, setTodoValue] = useState("");

  return (
    <header>
      <input
        placeholder="Enter Todo.."
        type="text"
        value={todoValue}
        onChange={(e) => {
          setTodoValue(e.target.value);
        }}
      />
      <button
        className="input-btn"
        onClick={() => {
          addTodo(todoValue);
          setTodoValue("");
        }}>
        Add
      </button>
    </header>
  );
}
