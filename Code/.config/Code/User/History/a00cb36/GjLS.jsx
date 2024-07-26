import React from "react";

export default function Search() {
  return (
    <div className="modSearch">
      <input type="text" name="search" placeholder="Mod Name" className="modSearchInput" />
      <button>
        <p>Search</p>
        <i className="fa-solid fa-magnifying-glass"></i>
      </button>
    </div>
  );
}
