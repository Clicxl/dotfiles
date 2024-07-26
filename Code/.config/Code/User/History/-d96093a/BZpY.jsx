import { useState } from "react";
import "./App.css";
import TodoInput from "./components/TodoInput";
import TodoList from "./components/TodoList";

function App() {
  const [todos, setTodos] = useState(['Do HW', "Eat Rice"]) //useState is used when user interacts with a variable

  function addTodo(newTodo){
    const newTodoList = [...todos, newTodo]
    setTodos(newTodoList)
  }


  return (
    <>
      <TodoInput addTodo={addTodo}/>
      <TodoList todos={todos}/>
    </>
  );
}

export default App;
