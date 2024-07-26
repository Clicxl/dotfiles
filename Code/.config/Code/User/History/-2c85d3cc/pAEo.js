const url = "https://api.modrinth.com/v2/"

async function getData(Baseurl, Name) {
  const mod_ids = {}
  const url = Baseurl + "search?query=" + `${Name}`
  try {
    const response = await fetch(url)
    if (response.status !== 200) {
      throw new Error(`Response failed ${response.status}`)
    }

    const data = await response.json()
    const mods = data.hits
    mods.forEach(mod => {
      // console.log(mod);
      mod_ids[mod.project_id] = {
        "ID": mod.project_id,
        "Title": mod.title, "Type": mod.categories, "Proj_Type": mod.project_type, "Version": mod.version, "Image": mod.icon_url
      }
    });

  }
  catch (err) {
    console.log(err.message);
  }

  return mod_ids
}

async function getMods(Baseurl, ID) {
  const url = Baseurl + "project/" + ID

  try {
    const response = await fetch(url)
    if (response.status !== 200) {
      throw new Error(`Response failed ${response.status}`)
    }

    const data = await response.json()

  }
  catch (err) {
    console.log(err.message);
  }
}


const modName = document.querySelector("#modName")
const modList = document.querySelector(".mods")
console.dir(modList)


modName.addEventListener("keydown", async (e) => {
  // console.log(e.key);
  if (e.key === "Enter") {
    console.log(modName.value);
    const mod = await getData(url, modName.value)
    console.log(mod);
    modList.append(`<div class='mod_${mod.name}'>
      <img src="${mod.Image}">
      </div>`)

  }

})
