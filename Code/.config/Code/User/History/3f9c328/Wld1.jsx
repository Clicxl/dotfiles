import Main from "./components/Main"
import Footer from "./components/Footer"
import SideBar from "./components/SideBar"
import { useState } from "react"

function App() {
  const NASA_KEY = import.meta.env.VITE_NASA_API_KEY
  const [showModal , setShowModal] = useState(false)
   function handelToggleModal() {
    setShowModal(!showModal)
   }

  return (
    <>
      <Main />
      {showModal && <SideBar handelToggleModal={handelToggleModal} />}
      <Footer handelToggleModal={handelToggleModal} />
    </>
  );
}

export default App
