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
                Desc: mod.description
            };
        });
    } catch (err) {
        console.log(err.message);
    }

    return mod_ids;
}

async function getMods(Baseurl, ID) {
    const fullurl = Baseurl + "project/" + ID;

    try {
        const response = await fetch(fullurl);
        if (response.status !== 200) {
            throw new Error(`Response failed ${response.status}`);
        }

        const data = await response.json();
    } catch (err) {
        console.log(err.message);
    }
}

const url = "https://api.modrinth.com/v2/";
const modName = document.querySelector("#modName");
const modList = document.querySelector(".mods");
console.dir(modList);

modName.addEventListener("keydown", async (e) => {
    // console.log(e.key);
    if (e.key === "Enter") {
        console.log(modName.value);
        const mods = await getData(url, modName.value, 5);
        console.log(mods);
        for (const key in mods) {
            modList.innerHTML += `<div class='mod_${mods[key]}'>
        <img src="${mods[key].Image}" class="modImage" alt="${mods[key].Title} Image">
        <div class"modInfo">
            <a href="#" class="modTitle">${mods[key].Title}</a>
            <p class="modDesc">${mods[key].Desc}</p>
        </div>
        </div>`;

        }

    }
});
