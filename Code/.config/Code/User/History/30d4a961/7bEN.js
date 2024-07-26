import { cornify_add } from "./cornify"
const pressed = []
const secretCode = 'clicxl'

window.addEventListener('keyup', (e) => {
    const key = e.key
    pressed.push(key)
    pressed.splice(-secretCode.length - 1, pressed.length - secretCode.length)
    // As more keys are pressed the initial ones will be poped out of thie list
    console.log(pressed)

    if (pressed.join("").includes(secretCode)) {
        console.log("Ding Ding !!!");
        cornify_add()
    }

})