import React, { useState } from "react";
import { getVersions } from "../utils";

export default function VersionSearch() {
  const [versions, setVersions] = useState();

  async function versionHandler() {
    const versionsList = (await getVersions()).filter((value, index) => {
      return value["type"] === "release" ? index : null;
    });

    const newVersionList = [];

    versionsList.forEach((version) => {
      newVersionList.push([version["id"], version["type"]]);
    });

    setVersions(await newVersionList);

    console.log(versions);
  }

  return (
    <div onClick={versionHandler}>
      <select name="" className="versionSearch">
      </select>
    </div>
  );
}
