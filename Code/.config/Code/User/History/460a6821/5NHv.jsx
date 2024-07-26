import React from "react";

export default function Loader() {
  return (
    <>
    <select className="modLoader">
      <p>Mod Loader</p>
      <option value="Fabric"></option>
      <option value="Forge"></option>
      <option value="Quilt"></option>
    </select>
    </>
  );
}
