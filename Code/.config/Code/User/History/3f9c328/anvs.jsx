import Main from "./components/Main"
import Footer from "./components/Footer"
import SideBar from "./components/SideBar"
import { useState } from "react"

function App() {
  const [showModal , setShowModal] = useState(false)

   function handelToggleModal() {
    setShowModal(!showModal)
   }

  return (
    <>
    <Main/>
    {showModal && (<SideBar/>)}
   function handelToggleModal() {
    <Footer />
    </>
  )
}

export default App
