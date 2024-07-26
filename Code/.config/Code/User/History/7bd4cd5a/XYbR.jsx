import { useState } from "react";
import Hero from "./components/Hero";
import Generator from "./components/Generator";
import Workout from "./components/Workout";

function App() {
  return (
    <main className="min-h-screen flex flex-col bg-gradient-to-r from-slate-800 to bg-slate-950 text-white text-sm sm:text-base">
      <Hero />
      <Generator />
      <Workout />
      <h1 className="text-3xl underline">Hello world!</h1>
    </main>
  );
}

export default App;
