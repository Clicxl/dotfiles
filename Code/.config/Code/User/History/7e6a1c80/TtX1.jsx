import React from "react";

export default function SectionWrapper(props) {
  const { children , header , title} = props;

  return (
  <section className="min-h-screen flex flex-col gap-10">
    {children}
    </section>
    )

}
