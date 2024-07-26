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

class Admin extends User {
    constructor(name) {
        super(name);
    }

    editData() {
        
    }
}

let student = new User("Student")
