import React from "react";

export default function Search() {
  return (
    <div className="modSearch">
      <i className="fa-solid fa-magnifying-glass"></i>
      <input
        type="text"
        name="search"
        placeholder="Mod Name"
        className="modSearchInput"
      />
    </div>
  );
}
