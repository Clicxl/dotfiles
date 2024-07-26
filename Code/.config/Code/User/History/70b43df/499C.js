const items = document.querySelectorAll(".item");

let fisrtSel = undefined;
let lastSel = undefined;

function getChecked(e){
    console.dir(e.target)
    if (e.target) {
        if (fisrtSel === undefined){
        fisrtSel = e.target
        return
    }

    if (fisrtSel !== undefined && lastSel === undefined){
        lastSel = e.target

    }

    console.log(fisrtSel,lastSel);}
}

// biome-ignore lint/complexity/noForEach: <explanation>
items.forEach((item) => item.addEventListener("change", getChecked));
