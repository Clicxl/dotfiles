const canvas = document.querySelector("#draw");
const ctx = canvas.getContext("2d");

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

ctx.strokeStyle = "#BADA55";
ctx.lineJoin = "round";
ctx.lineCap = "round";
ctx.lineWidth = 100

let isDrawing = false;
let [lastX,lastY] = [0,0];
let hue = 0;

function draw(e) {
	if (!isDrawing) return;
    ctx.strokeStyle = `hsl(${hue},100%,50%)`

	ctx.beginPath();
	ctx.moveTo(lastX, lastY);
	ctx.lineTo(e.offsetX, e.offsetY);
    ctx.stroke()

    updatePos(e)
    updateColor()
}

function updatePos(e){
    [lastX, lastY] = [e.offsetX, e.offsetY];
}

function updateColor(){
    if(!(hue>=360)){
    console.log(hue);
        hue++
    } else {hue = 1}
}

canvas.addEventListener("mousedown", (e) =>  {
    isDrawing = true;
    updatePos(e)
});

canvas.addEventListener("mousemove", draw);
canvas.addEventListener("mouseup", () => (isDrawing = false));
canvas.addEventListener("mouseout", () => (isDrawing = false));
