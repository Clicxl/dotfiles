const pressed = []
const secretCode = 'clicxl'

window.addEventListener('keyup', (e) => {
    const key = e.key
    pressed.push(key)
    pressed.splice(-secretCode.length - 1, pressed.length - secretCode.length)
    // As the 
})