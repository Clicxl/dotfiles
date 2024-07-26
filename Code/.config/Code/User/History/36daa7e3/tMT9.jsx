import React from "react";
import SectionWrapper from "./SectionWrapper";
import { WORKOUTS } from "../utils/swoldire";

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
  return (
    <SectionWrapper
      header={"Generate Your Workout"}
      title={["Its's", "Huge", "o'clock"]}>
      <Header
        index={"01"}
        title={"Pick your poison"}
        desc={"Select the workout you wish to endure."}
      />
      <div className="grid grid-cols-2 sm:grid-cols-4  gap-4">
        {Object.keys(WORKOUTS).map((type, typeIndex) => {
          return (
            <button
              key={typeIndex}
              className="bg-slate-950 py-3 rounded-lg duration-200 border border-transparent hover:border-blue-600">
              <p className="capitalize">{type.replaceAll("_", " ")}</p>
            </button>
          );
        })}
      </div>

      <Header
        index={"02"}
        title={"Lock on targets"}
        desc={"Select the muscles judged for annihilation."}
      />
      <div className="bg-slate-950 p-3 border border-solid border-blue-400 rounded-lg">
        <p>Select Muscle Groups</p>
        <i className="fa-solid fa-caret-down abosulte top-1/2 -translate-y-1/2 right-3"/>
      </div>
    </SectionWrapper>
  );
}
