import React, { useState } from "react";
import { getVersions } from "../utils";

export default function VersionSearch() {
  const [versions, setVersions] = useState();

  async function versionHandler() {
    const versionsList = await getVersions();

    const newVersionList = await versionsList.filter((value, index) => {
      return value["type"] === "release" ? index : null;
    });

    const Versions = []

    newVersionList.forEach(version => {
      for (const key in version) {
        Versions.push();
      }
    });

    console.log(await newVersionList);
  }

  return (
    <div onClick={versionHandler}>
      <select name="" className="versionSearch">
        {/* {versions.map((version) => { */}
        {/* return <option value={version["id"]}>{version["id"]}</option>; */}
        {/* })} */}
      </select>
    </div>
  );
}
