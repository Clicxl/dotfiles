import Main from "./components/Main"
import Footer from "./components/Footer"
import SideBar from "./components/SideBar"
import { useEffect, useState } from "react"

function App() {
  const [showModal , setShowModal] = useState(false)
  const [data,setData] = useState(null)
  const [loading, setLoading] = useState(false)

  function handelToggleModal() {
    setShowModal(!showModal)
   }

   useEffect(() => {
    async function fetchAPIData() {
      const NASA_KEY = import.meta.env.VITE_NASA_API_KEY
      const url = "https://api.nasa.gov/planetary/apod" + `?api_key=${NASA_KEY}`
      try {
        const response = await fetch(url)
        const apiData = await response.json()
        setData(apiData)

      }
      catch (error) {
        console.log(error.message);
      }
    }
    // fetchAPIData()
   }, [])

  return (
    <>
      {data ? (<Main />) :
      <div className="loadingState">
        <i className="fa-solid fa-gear"></i>
      </div>
      }
      {showModal && <SideBar handelToggleModal={handelToggleModal} />}
      <Footer handelToggleModal={handelToggleModal} />
    </>
  );
}

export default App
