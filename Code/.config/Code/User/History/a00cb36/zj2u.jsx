import React from "react";

export default function Search() {
  return (
    <div className="searchInput">
      <input type="text" name="search" placeholder="Mod Name" />
      <button>
        <p>Search</p>
        <i className="fa-solid fa-magnifying-glass"></i>
      </button>
    </div>
  );
}
