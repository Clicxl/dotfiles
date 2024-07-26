import React, { useState } from "react";
import Mod from "./Mod";

export default function Main(props) {
  const [inputVal, setInputVal] = useState("");

  // const {url} = props

  async function getData(Baseurl, Name, limit = 10) {
    const mod_ids = {};
    const fullurl = Baseurl + "search?" + `query=${Name}` + `&limit=${limit}`;
    try {
      const response = await fetch(fullurl);
      if (response.status !== 200) {
        throw new Error(`Response failed ${response.status}`);
      }

      const data = await response.json();
      console.log(data);

      const mods = data.hits;
      mods.forEach((mod) => {
        // console.log(mod);
        mod_ids[mod.project_id] = {
          ID: mod.project_id,
          Title: mod.title,
          Type: mod.categories,
          Proj_Type: mod.project_type,
          Version: mod.version,
          Image: mod.icon_url,
          Desc: mod.description,
        };
      });
    } catch (err) {
      console.log(err.message);
    }

    return mod_ids;
  }

  async function searchFunction(e) {
    if (e.key === "Enter") {
    }
  }

  const changeInputValue = (event) => {
    setInputVal(event.target.value);
  };

  return (
    <div>
      <input
        type="text"
        className="modInput"
        placeholder="Search"
        value={inputVal}
        onChange={changeInputValue}
        onKeyDown={searchFunction}
      />
    </div>
  );
}
