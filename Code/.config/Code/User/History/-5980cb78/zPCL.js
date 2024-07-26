const canvas = document.querySelector("#draw");
const ctx = canvas.getContext("2d");

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

ctx.strokeStyle = "#BADA55";
ctx.lineJoin = "round";
ctx.lineCap = "round";
ctx.lineWidth = 1;

let isDrawing = false;
let [lastX, lastY] = [0, 0];
let hue = 0;
let direction = true;
let compOperator = [
    "lighter",
	"multiply",
	"screen",
	"overlay",
	"darken",
	"lighten",
	"color-dodge",
	"color-burn",
	"hard-light",
	"soft-light",
	"difference",
	"exclusion",
];

ctx.globalCompostitionOperation = randChoice(compOperator)

function draw(e) {
	if (!isDrawing) return;
	ctx.strokeStyle = `hsl(${hue},100%,50%)`;

	ctx.beginPath();
	ctx.moveTo(lastX, lastY);
	ctx.lineTo(e.offsetX, e.offsetY);
	ctx.stroke();

	updatePos(e);
	updateCtx();
}

function updatePos(e) {
	[lastX, lastY] = [e.offsetX, e.offsetY];
}

function updateCtx() {
	if (hue >= 360) {
		hue = 1;
	}
	hue++;

	if (ctx.lineWidth >= 100 || ctx.lineWidth <= 1) {
		direction = !direction;
	}

	if (direction) {
		ctx.lineWidth++;
	} else {
		ctx.lineWidth--;
	}
}

function randChoice(list) {
	const num = Math.floor(Math.random() * list.lenght);
    return list[num]
}

canvas.addEventListener("mousedown", (e) => {
	isDrawing = true;
	updatePos(e);
});

canvas.addEventListener("mousemove", draw);
canvas.addEventListener("mouseup", () => (isDrawing = false));
canvas.addEventListener("mouseout", () => (isDrawing = false));
