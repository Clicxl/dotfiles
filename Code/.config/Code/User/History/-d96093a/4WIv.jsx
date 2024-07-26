import { useState, useEffect(() => {
  first

  return () => {
    second
  }
}, [third])
 } from "react";
import "./App.css";
import TodoInput from "./components/TodoInput";
import TodoList from "./components/TodoList";

function App() {
  const [todos, setTodos] = useState([]); //useState is used when user interacts with a variable
  const [todoValue, setTodoValue] = useState("");

  function persistData(newList) {
    localStorage.setItem("todos", JSON.stringify({ todos: newList }));
  }

  function addTodo(newTodo) {
    const newTodoList = [...todos, newTodo];
    persistData(newTodoList);
    setTodos(newTodoList);
  }

  function deleteTodo(index) {
    const newTodoList = todos.filter((todo, todoIndex) => {
      return todoIndex !== index;
    });
    persistData(newTodoList);
    setTodos(newTodoList);
  }

  function editTodo(index) {
    const valueToBeEdited = todos[index];
    persistData(newTodoList);
    setTodoValue(valueToBeEdited);
    deleteTodo(index);
  }


  return (
    <>
      <TodoInput addTodo={addTodo} todoValue={todoValue} setTodoValue={setTodoValue}/>
      <TodoList todos={todos} deleteTodo={deleteTodo} editTodo={editTodo} />
    </>
  );
}

export default App;
