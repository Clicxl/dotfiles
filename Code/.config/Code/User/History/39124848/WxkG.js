const student = {
    name: "Robert",
    marks: 76.9,
    totalMarks: 100

}

const Percent = {
    calPercent() {
        console.log((this.marks / this.totalMarks) * 100);
    },
};

student.__proto__ = Percent