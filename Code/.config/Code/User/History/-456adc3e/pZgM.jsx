import React from 'react'

export default function TodoList() {
  let todos = ['Make Rice', 'Cook']
  return (
    <ul style={margine-left:"20px"}>
      {todos.map((todo, index) => {
        return (
          <li>{todo}</li>
        )
      })}
    </ul>
  )
}
