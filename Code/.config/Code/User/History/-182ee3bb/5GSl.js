const panels = document.querySelectorAll(".panel");

function toggleOpen() {this.classList.toggle('open'); this.classList.toggle("color")}

function toggleActive(e) {
    if (e.propertyName === "flex-grow") {this.classList.toggle("open-active");}
}

function toggleHover() {
this.classList.toggle("open");
this.classList.toggle("color");
}

panels.forEach(panel => panel.addEventListener('click', toggleOpen))
panels.forEach((panel) => panel.addEventListener("mouseover", toggleHover));
panels.forEach((panel) => panel.addEventListener("transitionend", toggleActive));
