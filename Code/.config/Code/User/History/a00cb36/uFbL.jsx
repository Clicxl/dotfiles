import React from "react";
import styles from 

export default function Search() {
  return (
    <div className="modSearch">
      <i className="fa-solid fa-magnifying-glass" />
      <input
        type="text"
        name="search"
        placeholder="Mod Name"
        className="modSearchInput"
      />
    </div>
  );
}
