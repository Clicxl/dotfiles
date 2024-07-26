import React, { useState } from "react";
import { getVersions } from "../utils";

export default function VersionSearch() {
  const [versions, setVersions] = useState();

  async function versionHandler() {
    const versionsList = await getVersions();

    const newVersionList = await versionsList.filter((value, index) => {
      return value["type"] === "release" ? index : null;
    });

    const VerionList = Object.fromEntries(
      Object.entries(await newVersionList).map(([value, index]) => {
        return [value[0]]
      })
    );

    console.log(await VerionList);
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
