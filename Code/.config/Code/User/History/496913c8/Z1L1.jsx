import React, { useState } from "react";

export default function TodoInput(props) {
  const { addTodo } = props;
  const [todoValue, setTodoValue] = useState("");
  return (
    <header>
      <input
        type="text"
        name="todoinput"
        id="todoinput"
        value={todoValue}
        onChange={(e) => {
          setTodoValue(e.target.value);
        }}
      />
      <button
        onClick={() => {
          addTodo();
        }}>
        Add
      </button>
    </header>
  );
}
