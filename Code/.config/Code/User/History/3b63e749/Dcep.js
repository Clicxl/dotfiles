const dogs = [
	{ name: "Snickers", age: 2 },
	{ name: "hugo", age: 8 },
];

function makeGreen() {
	const p = document.querySelector("p");
	p.style.color = "#BADA55";
	p.style.fontSize = "50px";
}

// Regular
console.log("Hello World!!");

// Interpolated
console.log("This is %s the value", "interpolating"); // This %s is just like `` or f stings

// Styled
console.log(
	"%cAdd CSS to me",
	"font-size:50px; background-color:black; color:white; text-shadow:2px 2px 0 grey",
);
//%c can be used to change console.log messages with style using css

// warning!
console.warn("Oh NOOOOOOOOOOOO");

// Error :|
console.error("Shoot!");

// Info
console.info("Robert J Bomb 💣");

// Testing
console.assert(1 === 1, "6 - 5 = 2"); // This is to check before logging This fires only if the logic is wrong
console.assert(1 === 2, "You are Bad In Math"); // This is to check before logging This fires only if the logic is wrong

// clearing
// console.clear() // Clears the consle

// Viewing DOM Elements
const p = document.querySelector('p');
console.dir(p);

// Grouping together


// counting

// timing
