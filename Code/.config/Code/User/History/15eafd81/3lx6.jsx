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

    setVersions(newVersionList);
  }

  return (
    <div onClick={versionHandler}>
      <select name="" className="versionSearch">
        {versions.map((version) => {
          return <option value={version["id"]}>{version["id"]}</option>;
        })}
      </select>
    </div>
  );
}
