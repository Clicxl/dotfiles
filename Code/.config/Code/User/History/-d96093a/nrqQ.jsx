import { useState, useEffect } from "react";
import "./App.css";
import TodoInput from "./components/TodoInput";
import TodoList from "./components/TodoList";

function App() {
  const [todos, setTodos] = useState([]); //useState is used when user interacts with a variable
  const [todoValue, setTodoValue] = useState("");


  function addTodo(newTodo) {
    const newTodoList = [...todos, newTodo];
    setTodos(newTodoList);
  }

  function deleteTodo(index) {
    const newTodoList = todos.filter((todo, todoIndex) => {
      return todoIndex !== index;
    });
    setTodos(newTodoList);
  }

  function editTodo(index) {
    const valueToBeEdited = todos[index]
    setTodoValue(valueToBeEdited)
    deleteTodo(index)

  }

   useEffect(() => {
    if (!localStorage) return

    let localStorage = localStorage.getItem('todos')
   }, [])

  return (
    <>
      <TodoInput
        addTodo={addTodo}
        todoValue={todoValue}
        setTodoValue={setTodoValue}
      />
      <TodoList todos={todos} deleteTodo={deleteTodo} editTodo={editTodo} />
    </>
  );
}

export default App;
