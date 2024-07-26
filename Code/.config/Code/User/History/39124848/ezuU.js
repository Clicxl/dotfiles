class User {
    constructor(name) {
        this.name = name;
        this.email =  `${this.name}@email.com`;
        this.data = `${this.name} is using the server`
    }
    viewData() {
        console.log(`Name = ${this.name}`);
        console.log(`Email = ${this.email}`);

        console.log(this.data);
    }
}

class Admin extends User {
    constructor(name) {
        super(name);
    }

    editData(emailHost) {
        this.email = `${this.name}@${this.email}.com`;
        this.data = "Anonymous";
    }
}

let student = new User("Student");

let adminObj = new Admin("Admin Suresh");