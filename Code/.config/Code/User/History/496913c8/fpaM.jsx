import React, { useState } from 'react'

export default function TodoInput(props) {
  const {addTodo} = props
  const [todoValue , setTodoValue] = useState("")

  const btn = document.querySelector('button')
  return (
    <header>
      <input type="text" value={todoValue} onChange={(e) => {
        setTodoValue(e.target.value)
      }}/>
      <button onClick={() => {
        addTodo(todoValue)
      } className=""}>Add</button>
    </header>
  )
}
