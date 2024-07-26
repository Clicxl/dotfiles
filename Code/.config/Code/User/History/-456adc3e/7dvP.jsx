import React from 'react'

export default function TodoList() {
  let todos = ['Make Rice', 'Cook']
  return (
    <ul className='main'>
      {todos.map((todo, index) => {
        return (
          <li key={index} className='todoItem'>{todo}</li>
        )
      })}
    </ul>
  )
}
