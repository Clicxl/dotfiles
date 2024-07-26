import React from 'react'

export default function TodoInput(props) {
  const {addTodo} = props
  return (
    <header>
      <input type="text" name="todoinput" id="todoinput" />
      <button>Add</button>
    </header>
  )
}
