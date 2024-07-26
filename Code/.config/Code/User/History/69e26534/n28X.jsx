import React from "react";

export default function TodoCard(props) {
  const { children, deleteTodo, index} = props;
  return (
    <li className="todoItem">
      {children}
      <div className="actionsContainer">
        <i className="fa-solid fa-pen-to-square"></i>
        <i className="fa-solid fa-trash" onClick={() => {
          deleteTodo(index);
        }}></i>
      </div>
    </li>
  );
}
