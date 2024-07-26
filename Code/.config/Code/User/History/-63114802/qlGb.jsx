import React from "react";

export default function SideBar(props) {
  const { handelToggleModal, data } = props;
  return (
    <div className="sideBar">
      <div className="bgOverlay"></div>
      <div className="sideBarContent">
        <div className="descriptionContainter">
          <h2>{data?.title}</h2>
          <p className="descriptionTitle">Description</p>
          <p>{data?.explanation}</p>
        </div>
        <button className="exitBtn" onClick={handelToggleModal}>
          <i className="fa-solid fa-arrow-right"></i>
        </button>
      </div>
    </div>
  );
}
