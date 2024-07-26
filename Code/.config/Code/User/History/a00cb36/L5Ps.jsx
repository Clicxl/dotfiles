import React from "react";

export default function Search() {
  return (
    <div className="search-input">
      <input type="text" name="search" placeholder="Search the Mod"></input>
      <button>
        <p>Search</p>
        <i className="fa-solid fa-magnifying-glass"></i>
      </button>
    </div>
  );
}
