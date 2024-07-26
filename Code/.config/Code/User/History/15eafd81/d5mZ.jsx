import React, { useState } from "react";
import { getVersions } from "../utils";

export default function VersionSearch() {
  const [versions, setVersions] = useState();

  async function versionHandler() {
    const versionsList = await getVersions();

    const newVersionList = await versionsList.filter((value, index) => {
      return value["type"] === "release" ? index : null;
    });

    const Versions = [];

    newVersionList.forEach((version) => {
      Versions.push([version["id"], version["type"]]);
    });

    console.log(await Versions);
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
