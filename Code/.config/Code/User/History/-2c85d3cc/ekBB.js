const mod_id = {}
const url = "https://api.modrinth.com/v2/"

async function getData(Baseurl, Name) {
  const url = Baseurl + "search?query=" + `${Name}`
  try {
    const response = await fetch(url)
    if (response.status !== 200) {
      throw new Error(`Response failed ${response.status}`)
    }

    const data = await response.json()
    const mods = data.hits
    mods.forEach(mod => {
      mod_id[mod.project_id] = {
        "ID": mod.project_id,
        "Title": mod.title, "Type": mod.categories, "Proj_Type": mod.project_type, "Version": mod.version
      }
    });

  }
  catch (err) {
    console.log(err.message);
  }

  return mod_id
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

modName.addEventListener("keydown", (e) => {
  console.log(e.key);
  if (e.key === "Enter") {
    console.log("Hi");
  }

})
