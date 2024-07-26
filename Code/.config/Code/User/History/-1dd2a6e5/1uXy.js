// Access all the player elements
const player = document.querySelector(".player")
const video = player.querySelector(".viewer")

const progress = player.querySelector(".progress")
const progressBar = player.querySelector(".progress__filled")


const playBtn = player.querySelector(".player__button");

const skiBtn = player.querySelectorAll("button[data-skip]")

const volume = player.querySelector("input[name='volume']")
const playBack = player.querySelector("input[name='playbackRate']")

// Player functions
function togglePlay() {
    const method = video.paused ? 'play' : 'pause';
    video[method]()
}

function updateBtn() {
    const icon = this.paused ? '▶' : "❚ ❚"
    playBtn.textContent = icon
}

function skip() {
    video.currentTime += parseFloat(this.dataset.skip)
}

// Hook up the event listener
video.addEventListener('click', togglePlay)
document.querySelector('body').addEventListener('keydown', e => {
    const key = e.key

    if (key === "space") {
        console.log("playing");
        togglePlay()
    }
})
video.addEventListener('play', updateBtn)
video.addEventListener('pause', updateBtn)

playBtn.addEventListener('click', togglePlay)

skiBtn.forEach(button => button.addEventListener('click', skip))