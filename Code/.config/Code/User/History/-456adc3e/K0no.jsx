import React from 'react'

export default function TodoList() {
  let todos = ['Make Rice', 'Cook']
  return (
    <ul >
      {todos.map((todo, index) => {
        return (
          <li key={index}>{todo}</li>
        )
      })}
    </ul>
  )
}
