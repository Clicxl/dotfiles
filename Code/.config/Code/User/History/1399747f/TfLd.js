export async function getData(Baseurl, Name, limit = 10) {
  const mod_ids = [];
  const fullurl = Baseurl + "search?" + `query=${Name}` + `&limit=${limit}`;
  try {
    const response = await fetch(fullurl);
    if (response.status !== 200) {
      throw new Error(`Response failed ${response.status}`);
    }

    const data = await response.json();

    const mods = data.hits;
    mods.forEach((mod) => {
      // console.log(mod);
      mod_ids.push({
        ID: mod.project_id,
        Title: mod.title,
        Type: mod.categories,
        Proj_Type: mod.project_type,
        Version: mod.version,
        Image: mod.icon_url,
        Desc: mod.description,
      });
    });
  } catch (err) {
    console.log(err.message);
  }

  return mod_ids;
}

export async