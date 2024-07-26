let marks = [250,640,300,900,50];
let offer = 10/100;

for ( let idx in marks) {
    marks[idx] = marks[idx] - (offer * marks[idx])
}

console.log(marks)