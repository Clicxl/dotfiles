import React from 'react'

export default function TodoList() {
  let todos = ['Make Rice', 'Cook']
  return (
    <div>
      {todos.map((todo, index) => {
        return (
          <li>{todo}</li>
        )
      })}
    </div>
  )
}
