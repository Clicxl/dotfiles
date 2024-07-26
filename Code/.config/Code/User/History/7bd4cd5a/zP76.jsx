import { useState } from 'react'
import Hero from './components/Hero'
import Generator from './components/Generator'
import Workout from './components/Workout'


function App() {

  return (
    <main className='min-h-screen flex flex-col bg-gradient'>
    <Hero />
    <Generator />
    <Workout />
    </main>
  )
}

export default App
