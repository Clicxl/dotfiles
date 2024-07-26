class User {
    constructor(name) {
        this.name = name;
        this.email =  `${this.name}@gmail.com`;
    }
    viewData() {
        console.log(`Name = ${this.name}`);
        console.log(`Email = ${this.email}`);
    }
}

