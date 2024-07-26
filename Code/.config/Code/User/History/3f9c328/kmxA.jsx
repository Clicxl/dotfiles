import Main from "./components/Main"
import Footer from "./components/Footer"
import SideBar from "./components/SideBar"
import { useState } from "react"

function App() {
  const [showModel , setShowModel] = useState(false)


  return (
    <>
    <Main/>
    {showModel && (<SideBar/>)}
    <Footer/>
    </>
  )
}

export default App
