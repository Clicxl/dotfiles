let marks = [250,640,300,900,50];
let offer = 10/100;

for ( let val of marks) {
    sum += val;
}

let avg = sum / marks.length
console.log(`Avg marks = ${avg}`)