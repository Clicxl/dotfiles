// Access all the player elements
const body = document.querySelector('body')

const player = document.querySelector(".player")
const video = player.querySelector(".viewer")

const progress = player.querySelector(".progress")
const progressBar = player.querySelector(".progress__filled")


const playBtn = player.querySelector(".player__button");

const skipBtn = player.querySelectorAll("button[data-skip]")

const ranges = player.querySelectorAll(".player__slider")

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
    video.currentTime += Number.parseFloat(this.dataset.skip)
}

function handleRangeUpdate() {
    console.log(this.value);
}

// Hook up the event listener
video.addEventListener('click', togglePlay)

body.addEventListener('keydown', e => {
    const key = e.key
    if (key === " ") togglePlay();

})



video.addEventListener('play', updateBtn)
video.addEventListener('pause', updateBtn)

playBtn.addEventListener('click', togglePlay)

// biome-ignore lint/complexity/noForEach: <explanation>
skipBtn.forEach(button => button.addEventListener('click', skip))

// biome-ignore lint/complexity/noForEach: <explanation>
skipBtn.forEach(() => body.addEventListener('keydown', (e) => {
    const key = e.key
    if (key==="ArrowRight"){
        video.currentTime += Number.parseFloat("25");
    }else if (key === "ArrowLeft") {
        video.currentTime += Number.parseFloat("-10");
    }
}))

ranges.forEach(range => range.addEventListener('change',handleRangeUpdate))
ranges.forEach(range => range.addEventListener('mousemove', handleRangeUpdate))