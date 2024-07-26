import Tracker from "./Tracker.tsx"

export default function Main() {

  return (
    <div className='Main'>
      <div className="imgContainer">
        <div className="bgOverlay"></div> 
        <img src="./public/background-image.jpg" alt="background-image" className="bgImage"/>
      </div>
      <Tracker />

    </div>
  )
}
