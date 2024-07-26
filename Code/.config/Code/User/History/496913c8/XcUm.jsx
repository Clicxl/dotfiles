import React, { useState } from 'react'

export default function TodoInput(props) {
  const {addTodo} = props
  const [todoValue , setTodoValue] = useState
  return (
    <header>
      <input type="text" name="todoinput" id="todoinput" />
      <button onClick={() => {
        addTodo()
      }}>Add</button>
    </header>
  )
}
