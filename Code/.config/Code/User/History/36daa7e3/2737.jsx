import React, { useState } from "react";
import SectionWrapper from "./SectionWrapper";
import { SCHEMES, WORKOUTS } from "../utils/swoldire";

function Header(props) {
  const { index, title, desc } = props;
  return (
    <div className="flex flex-col gap-4">
      <div className="flex items-center justify-center gap-2">
        <p className="text-3xl sm:text-4xl md:text-5xl lg:text-6xl font-semibold text-slate-400 p-4">
          {index}
        </p>
        <h2 className="text-xl sm:text-2xl md:text-3xl lg:text-4xl ">
          {title}
        </h2>
      </div>
      <p className="text-sm sm:text-base mx-auto">{desc}</p>
    </div>
  );
}

export default function Generator() {
  const [showModal, setShowModal] = useState(false);
  const [poison, setPoison] = useState("individual");
  const [muscles, setMuscles] = useState([]);
  const [goal, setGoal] = useState("strength_power");

  return (
    <SectionWrapper
      header={"Generate Your Workout"}
      title={["Its's", "Huge", "o'clock"]}>
      <Header
        index={"01"}
        title={"Pick your poison"}
        desc={"Select the workout you wish to endure."}
      />
      <div className="grid grid-cols-3 gap-4">
        {Object.keys(SCHEMES).map((scheme, schemeIndex) => {
          return (
            <button
              key={schemeIndex}
              className="bg-slate-950 py-3 rounded-lg duration-200 border border-transparent hover:border-blue-600">
              <p className="capitalize">{scheme.replaceAll("_", " ")}</p>
            </button>
          );
        })}
      </div>

      <Header
        index={"02"}
        title={"Lock on targets"}
        desc={"Select the muscles judged for annihilation."}
      />
      <div className="bg-slate-950 border border-solid border-blue-400 rounded-lg flex flex-col">
        <button
          onClick={(event) => {
            setShowModal(!showModal);
          }}
          className="relative p-3 flex items-center justify-center ">
          <p>Select Muscle Groups</p>
          <i className="fa-solid absolute right-3 top-1/2 -translate-y-1/2 fa-caret-down" />
        </button>
        {showModal && <div>modal</div>}
      </div>

      <Header
        index={"03"}
        title={"Lock on targets"}
        desc={"Select the muscles judged for annihilation."}
      />
      <div className="bg-slate-950 border border-solid border-blue-400 rounded-lg flex flex-col">
        <button
          onClick={(event) => {
            setShowModal(!showModal);
          }}
          className="relative p-3 flex items-center justify-center ">
          <p>Select Muscle Groups</p>
          <i className="fa-solid absolute right-3 top-1/2 -translate-y-1/2 fa-caret-down" />
        </button>
        {showModal && <div>modal</div>}
      </div>
    </SectionWrapper>
  );
}
