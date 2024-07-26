import React, { useState } from 'react'

export default function TodoInput(props) {
  const {addTodo} = props
  const [todoValue , setTodoValue] = useState("")

  const btn = document.querySelector('.input-btn')
  window.addEventListener('keydown', (e) => {
    if (e.key === 'enter') {
      setTodoValue()
    }
  })
  return (
    <header>
      <input type="text" value={todoValue} onChange={(e) => {
        setTodoValue(e.target.value)
      }}/>
      <button className='input-btn' onClick={() => {
        addTodo(todoValue)
      } }>Add</button>
    </header>
  )
}
