import React from "react";

export default function SectionWrapper(props) {
  const { childern } = props;
  console.log(childern);
  return <div>{childern}</div>;
}
