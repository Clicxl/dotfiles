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
    const fullurl = Baseurl + "version/" + ID;

    try {
        const response = await fetch(fullurl);
        if (response.status !== 200) {
            throw new Error(`Response failed ${response.status}`);
        }

        const data = await response.json();
        console.log(data);
        // console.log(`https://api.modrinth.com/v2/version/${version_id}/file/${file_name}`);
    } catch (err) {
        console.log(err.message);
    }
}

const url = "https://api.modrinth.com/v2/";


modName.addEventListener("keydown", async (e) => {
    if (e.key === "Enter") {
        const mods = await getData(url, modName.value, 5);
        modList.innerHTML = ""
        for (const key in mods) {
            const downMods = await getMods(url,key)
            // console.log(downMods);


            modList.innerHTML += ;

        }

    }
});
