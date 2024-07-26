const items = document.querySelectorAll(".inbox input['type=checkbox']");

let lastCheck;

function getChecked(e) {
    let inBetween = false;

	if (e.shiftKey && this.checked) {
        items.forEach(item => )
	}
	lastCheck = this;
}

function stackSearch() {}

// biome-ignore lint/complexity/noForEach: <explanation>
items.forEach((item) => item.addEventListener("click", getChecked));
