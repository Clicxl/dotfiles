const items = document.querySelectorAll(".item");

let fisrtSel = undefined;
let lastSel = undefined;

function getChecked(e){
    console.dir(e);
    if (fisrtSel !== undefined) return
    fisrtSel = e.target

}

// biome-ignore lint/complexity/noForEach: <explanation>
items.forEach((item) => item.addEventListener("change", getChecked));