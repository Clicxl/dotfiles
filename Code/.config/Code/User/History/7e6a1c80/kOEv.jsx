import React from "react";

export default function SectionWrapper(props) {
  const { children, header, title } = props;

  return (
    <section className="min-h-screen flex flex-col gap-10">
      <div className="bg-slate-950 py-10 flex felx-col gap-4 justify-center align-center"></div>
    </section>
  );
}
