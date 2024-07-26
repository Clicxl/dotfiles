const items = document.querySelectorAll(".inbox input['type=checkbox']");

let fisrtSel = undefined;
let lastSel = undefined;

function getChecked(e) {
	if (e.target.checked) {
		if (fisrtSel === undefined) {
			fisrtSel = e.target;
			return;
		}

		if (fisrtSel !== undefined && lastSel === undefined) {
			lastSel = e.target;
		}
	} else {
		if (fisrtSel !== undefined) {
			fisrtSel = undefined;
			return;
		}

		if (fisrtSel === undefined && lastSel !== undefined) {
			lastSel = undefined;
		}
	}
}

function stackSearch() {}

// biome-ignore lint/complexity/noForEach: <explanation>
items.forEach((item) => item.addEventListener("click", getChecked));
