const items = document.querySelectorAll(".item");

let lastCheck;

function getChecked(e) {
	let inBetween = false;
    console.log(e.shiftKey,this.checked);
    console.log(this.checked);
	if (e.shiftKey && this.checked) {
		// biome-ignore lint/complexity/noForEach: <explanation>
		items.forEach((item) => {
			console.log(item);
			if (item === this || item === lastCheck) {
				inBetween = !inBetween;
			}
		});
	}
	lastCheck = this;
}

function stackSearch() {}

// biome-ignore lint/complexity/noForEach: <explanation>
items.forEach((item) => item.addEventListener("click", getChecked));
