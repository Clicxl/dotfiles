const items = document.querySelectorAll(".inbox input['type=checkbox']");

let lastCheck;

function getChecked(e) {
	let inBetween = false;

	if (e.shiftKey && this.checked) {
		items.forEach((item) => {
			if (item === this || item === lastCheck) {
			}
		});
	}
	lastCheck = this;
}

function stackSearch() {}

items.forEach((item) => item.addEventListener("click", getChecked));
