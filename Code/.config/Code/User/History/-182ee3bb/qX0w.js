const panels = document.querySelectorAll(".panels");

function toggleOpen() {
    this.classList.add('.open')
}

panels.forEach(panel => panel.addEventListener('click', toggleOpen))