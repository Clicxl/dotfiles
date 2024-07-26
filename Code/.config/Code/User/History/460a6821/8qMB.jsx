import React from "react";
import "./CSS/Loader.css"

export default function Loader() {
  return (
    <>
    <select className="modLoader">
      <option value="Fabric">Fabric</option>
      <option value="Forge">Forge</option>
      <option value="Quilt">Quilt</option>
    </select>
    </>
  );
}
