import React from 'react'

export default function TodoCard() {
  return (
    <li className="todoInput">
      <div className="actionsContainer">
        <i className="fa-solid fa-pen-to-square"></i>
        <i className="fa-solid fa-trash"></i>
      </div>
    </li>
  );
}
