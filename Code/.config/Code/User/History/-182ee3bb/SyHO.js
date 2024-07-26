const panels = document.querySelectorAll(".panel");

function toggleOpen() {this.classList.toggle('open'); this.style.filter = none;}

function toggleActive(e) {
    if (e.propertyName === "flex-grow") {this.classList.toggle("open-active");}
}


panels.forEach(panel => panel.addEventListener('click', toggleOpen))
panels.forEach((panel) => panel.addEventListener("transitionend", toggleActive));
