const items = document.querySelectorAll(".item");

let fisrtSel = undefined;
let lastSel = undefined;

function getChecked(e){
    if (e.target.checked) {
					if (fisrtSel === undefined) {
						fisrtSel = e.target;
						return;
					}

					if (fisrtSel !== undefined && lastSel === undefined) {
						lastSel = e.target;
					}

					console.log(fisrtSel, lastSel);
				}else {
                    					if (fisrtSel === undefined) {
						fisrtSel = e.target;
						return;
					}

					if (fisrtSel !== undefined && lastSel === undefined) {
						lastSel = e.target;
					}
                }
}

// biome-ignore lint/complexity/noForEach: <explanation>
items.forEach((item) => item.addEventListener("change", getChecked));
