import React from "react";

export default function SideBar() {
  return (
    <div className="sideBar">
      <div className="bgOverlay"></div>
      <div className="sideBarContent">
        <h2>The Brutal Martian Landscape</h2>
        <div>
          <p>Description</p>
          <p>
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Ut, natus.
          </p>

        </div>
          <button className="exitBtn">
            <i className="fa-solid fa-arrow-right"></i>
          </button>
      </div>
    </div>
  );
}
