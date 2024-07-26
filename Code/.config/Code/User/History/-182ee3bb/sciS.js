const panels = document.querySelectorAll(".panel");

function toggleOpen() {
    this.classList.add('.open')
}

panels.forEach(panel => panel.addEventListener('click', toggleOpen))