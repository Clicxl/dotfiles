import React from "react";

export default function TodoCard(props) {
  const { children, deleteTodo , key } = props;
  return (
    <li className="todoItem">
      {children}
      <div className="actionsContainer">
        <i className="fa-solid fa-pen-to-square"></i>
        <i className="fa-solid fa-trash" onClick={() => {
          console.log("Deleting");
          deleteTodo(key)
        }}></i>
      </div>
    </li>
  );
}
