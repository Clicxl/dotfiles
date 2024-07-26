import React from 'react'

export default function Mod() {
  return (
  <div class='mod_${mods[key].Title}'>
        <img src="${mods[key].Image}" class="modImage" alt="${mods[key].Title} Image">
            <div class"modInfo">
                <a href="#" class="modTitle">${mods[key].Title} · <span>${mods[key].Proj_Type}</span></a>
                <p class="modDesc">${mods[key].Desc}</p>
            </div>
            <button class="DownloadBtn">
            <i class="fa-solid fa-arrow-down"></i>
            </button>
    </div>;
  )
}
