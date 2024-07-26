
const keyPress = document.addEventListener("keydown", (e) => {

    const audio = document.querySelector(`audio[data-key="${e.keyCode}"]`);
    const key = document.getElementsByClassName('key',`div[data-key="${e.keyCode}]`);

    if (!audio) return;
    audio.play();
    console.log(key);

})

