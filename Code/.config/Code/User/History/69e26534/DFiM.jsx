import React from "react";

export default function TodoCard(props) {
  const { children, deleteTodo, index, editTodo} = props;
  return (
    <li className="todoItem">
      {children}
      <div className="actionsContainer">
        <button>
          <i className="fa-solid fa-pen-to-square" onClick={() => {
            editTodo(index)
          }}></i>
        </button>
        <button>
        <i
          className="fa-solid fa-trash"
          onClick={() => {
            deleteTodo(index);
          }}></i>
        </button>
      </div>
    </li>
  );
}
