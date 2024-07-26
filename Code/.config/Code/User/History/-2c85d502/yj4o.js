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
    const IDS = [ID, ID]
    // GET https://api.modrinth.com/v2/version?ids=["AABBCCDD", "EEFFGGHH"]
    const fullurl = `${Baseurl}/version?ids=${IDS}`;

    try {
        const response = await fetch(fullurl);
        if (response.status !== 200) {
            throw new Error(`Response failed ${response.status}`);
        }

        const data = await response.json();
        console.log(data);
    } catch (err) {
        console.log(err.message);
    }
}

const url = "https://api.modrinth.com/v2/";





const modName = document.querySelector(".modInput");
const modList = document.querySelector(".mods");

modName.addEventListener("keydown", async (e) => {
    if (e.key === "Enter") {
        const mods = await getData(url, modName.value, 5);
        modList.innerHTML = ""
        for (const key in mods) {
            const downMods = await getMods(url,mods[key].ID)
            // console.log(downMods);


            modList.innerHTML += `<div class='mod_${mods[key].Title}'>
        <img src="${mods[key].Image}" class="modImage" alt="${mods[key].Title} Image">
            <div class"modInfo">
                <a href="#" class="modTitle">${mods[key].Title} · <span>${mods[key].Proj_Type}</span></a>
                <p class="modDesc">${mods[key].Desc}</p>
            </div>
            <button class="DownloadBtn">
            <i class="fa-solid fa-arrow-down"></i>
            </button>
        </div>`;

        }

    }
});
