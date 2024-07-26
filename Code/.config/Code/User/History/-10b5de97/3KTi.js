let marks = [250,640,300,900,50];
let offer = (100 - prompt("Enter Offer in %"))/100;

for ( let idx in marks) {
    marks[idx] *= offer
}

console.log(marks)