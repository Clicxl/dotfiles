import React, { useState } from "react";
import { getVersions } from "../utils";

export default function VersionSearch() {
  const [versions, setVersions] = useState();

  async function versionHandler() {
    const versionsList = await getVersions();
    setVersions(
      await versionsList.filter((value, index) => {
        return value["type"] === "release" ? index : null;
      })
    );
    console.log(versions);
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
