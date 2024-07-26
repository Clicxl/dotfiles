const items = document.querySelectorAll(".inbox input[type='checkbox']");

let lastCheck;

function getChecked(e) {
	let inBetween = false;
	if (e.shiftKey && this.checked) {
		// biome-ignore lint/complexity/noForEach: <explanation>
		items.forEach((item) => {
			if (item === this || item === lastCheck) {
				inBetween = !inBetween;
				console.log(item);
			}

			if (inBetween) {
				item.checked = true;
			}
		});
	}
	lastCheck = this;
}

function stackSearch() {}

// biome-ignore lint/complexity/noForEach: <explanation>
items.forEach((item) => item.addEventListener("click", getChecked));
