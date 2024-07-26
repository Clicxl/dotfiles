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
    video[this.name] = this.value
}

function handleProgress(){
    const percent = (video.currentTime / video.duration) * 100;
    progressBar.style.flexBasis = `${percent}%`
}


function scrub(e) {
    const scrubTime = (e.offsetX / progress.offsetWidth) * video.duration
    video.currentTime = scrubTime
}

// Hook up the event listener
video.addEventListener('click', togglePlay)

body.addEventListener('keydown', e => {
    const key = e.key
    if (key === " ") togglePlay();

})

video.addEventListener('play', updateBtn)
video.addEventListener('pause', updateBtn)
video.addEventListener('timeupdate', handleProgress)

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

// biome-ignore lint/complexity/noForEach: <explanation>
ranges.forEach(range => range.addEventListener('change',handleRangeUpdate))
// biome-ignore lint/complexity/noForEach: <explanation>
ranges.forEach(range => range.addEventListener('mousemove', handleRangeUpdate))


let mouseDown = false;
progress.addEventListener('click',scrub)
progress.addEventListener('mousemove', (e) => mouseDown && scrub(e))
// biome-ignore lint/suspicious/noAssignInExpressions: <explanation>
progress.addEventListener('mousedown', () => mouseDown = true)
// biome-ignore lint/suspicious/noAssignInExpressions: <explanation>
progress.addEventListener('mouseup', () => mouseDown = false)