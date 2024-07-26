const items = document.querySelectorAll(".inbox input['type=checkbox']");

let lastCheck;

function getChecked(e) {
	if (e.shiftKey && this.checked) {
            
	}
	lastCheck = this;
}

function stackSearch() {}

// biome-ignore lint/complexity/noForEach: <explanation>
items.forEach((item) => item.addEventListener("click", getChecked));
