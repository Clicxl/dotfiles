import React from 'react'

export default function Search() {
  return (
    <div className="search-input">
      <input type="text" name="search" placeholder='Search the Mod'>
      <i className="fa-solid fa-magnifying-glass"></i>
      </input>
      <button>Search</button>
    </div>
  )
}
