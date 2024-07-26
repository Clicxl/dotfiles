import React from "react";
import "./CSS/Loader.css";

export default function Loader() {
  return (
    <>
      <div className="Loader">
        <select className="modLoader">
          <option value="Fabric" className="">Fabric</option>
          <option value="Forge" >Forge</option>
          <option value="Quilt" >Quilt</option>
        </select>
      </div>
    </>
  );
}
