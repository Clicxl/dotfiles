
const keyPress = document.addEventListener("keydown", (e) => {

    const audio = document.querySelector(`audio[data-key="${e.keyCode}"]`);
    const key = document.querySelector(`.key[data-key="${e.keyCode}"]`);

    if (!audio) return;
    audio.currentTime = 0;
    audio.play();
    key.classList.add("clicked")


})


function removeTranistion(e) {
    if (e.propertyName !== "transform") return;
    this.classList.remove("clicked")
}

const keys = document.querySelectorAll(".key");
keys.forEach(key => key.addEventListener("transitionend",removeTranistion));
