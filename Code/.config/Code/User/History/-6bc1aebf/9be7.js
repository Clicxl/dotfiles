
const keyPress = document.addEventListener("keydown", (e) => {

    const audio = document.querySelector(`audio[data-key="${e.keyCode}"]`);
    const keyDiv = document.querySelector)

    if (!audio) return;
    audio.play();

})

