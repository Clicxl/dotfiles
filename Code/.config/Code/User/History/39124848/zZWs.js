class User {
    constructor(name) {
        this.name = name;
        this.email =  `${this.name}@email.com`;
    }
    viewData() {
        console.log(`Name = ${this.name}`);
        console.log(`Email = ${this.email}`);
    }
}

let student = new User("Student")
