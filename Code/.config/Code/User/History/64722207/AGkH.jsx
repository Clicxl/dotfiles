import React from "react";
import Search from "./Search";
import Loader from "./Loader";

export default function Main() {
  return (
    <>
      <div className="Main">
        <div className="Input">
          <Search />
          <Loader />
        </div>
      </div>
    </>
  );
}
