//Challenge 1 - Basics

let newString: string = "Hello World";
newString = newString.toUpperCase();
// console.log(newString);

let newNumber: number = 234;
console.log(45 + newNumber);
// console.log(newNumber.toString());

let isBool: boolean = true;
if (isBool) {
  // console.log(!isBool);
}

// newString = 234;
// newNumber = "Hello"
// isBool = "Not Bool"
// console.log(newString,newNumber,isBool);

//Challenge 2 - Union Type
let orderStatus: "processing" | "shipped" | "delivered" = "processing";
orderStatus = "shipped";
orderStatus = "delivered";
// orderStatus = 'returned'
// console.log(orderStatus);

let discount: number | string = 20;
discount = "20%";
console.log(discount);

//Challenge 3 - Arrays
let temperature: number[] = [34, 53];
// temperature.push("hot");

let colors: string[] = ["blue", "red"];
// colors.push(false);

let mixedArray: (string | number)[] = [1, 54, "hello"];
// mixedArray.push(true);

//Challenge 4 - Objects
let bike: { brand: string; year: number } = { brand: "Hero", year: 1956 };
// bike.brand = 4

// let laptop: { brand: string; year: number } = { brand: "dell", year: 2020 };
let laptop2: { brand: string; year: number } = { brand: "dell", year: 2020 };

let product1 = { title: "Shirt", price: 20 };
let product2 = { title: "Pants" };
let product: { title: string; price?: number }[] = [product1, product2];
// product[0].price = '30';

//Challenge 5 - Function
let names: string[] = ["KP", "Hari", "Mithun", "Jeet", "Kesha"];

function isName(name: string): boolean {
  return names.includes(name);
}

let name1: string = "Jeet";
isName(name1)
  ? console.log(`${name1} is Present`)
  : console.log(`${name1} is not Present`);

//Challenge 6 - Optional and Default Parameters
function processInput(input: string | number): void {
  if (typeof input === "number") {
    console.log(input * 2);
  } else {
    console.log(input.toUpperCase());
  }
}

processInput(30);
processInput("Hello");

//Challenge 7 - Using Objects as Function Parameters
function procesData(
  input: string | number,
  config: { reverse: boolean } = { reverse: false }
): number | string {
  if (typeof input === "number") {
    return input ** 2;
  } else {
    return config.reverse === true
      ? input.toUpperCase().split("").reverse().join("")
      : input.toUpperCase();
  }
}

console.log(procesData(10));
console.log(procesData("Hello"));
console.log(procesData("Hello", { reverse: true }));

//Challenge 8 - Type Alias
type Empolyee = {
  id: number;
  name: string;
  department: string;
};

type Manager = {
  id: number;
  name: string;
  employees: Empolyee[];
};

type Staff = Empolyee | Manager;

function printStaffDetails(staff: Staff): void {
  if ("employees" in staff) {
    console.log(`ID: ${staff.id}`);
    console.log(`Name: ${staff.name}`);
    staff.employees.forEach((employee) => {
      console.log(`People Working Under: ${employee.id} | ${employee.name} `);
    });
  } else {
    console.log(`ID: ${staff.id}`);
    console.log(`Name: ${staff.name}`);
    console.log(`Dept: ${staff.department}`);
  }
}

const alice: Empolyee = { id: 1, name: "alice", department: "sales" };
const mary: Empolyee = { id: 2, name: "mary", department: "marketing" };
const robert: Empolyee = { id: 3, name: "robert", department: "design" };

const john: Manager = { id: 4, name: "john", employees: [alice, mary, robert] };

printStaffDetails(alice);
printStaffDetails(john);

//Challenge 9 - Interface
interface Computer {
  readonly id: number;
  brand: string;
  ram: number;
  storage?: number;
  upgradeRam(amount: number): number; // You cannot Define the logic of the command in interface
}

const laptop: Computer = {
  id: 1,
  brand: "Dell",
  ram: 16,
  upgradeRam(amount: number): number {
    return this.ram + amount;
  },
};

laptop.storage = 256;

console.log(laptop.upgradeRam(16) + " GB of RAM");
console.log(laptop);

//Challenge 10 - Interface Merging, Extend, TypeGuard
interface Person {
  name: string;
}

interface DogOwner extends Person {
  dogName: string;
}

interface CompManager extends Person {
  managePeople(): void;
  delegateTasks(): void;
}

function getEmployee(): Person | DogOwner | CompManager {
  const random = Math.random();
  if (random < 0.33) {
    return { name: "Bibi" };
  } else if (random < 0.66) {
    return { name: "Rubertuto", dogName: "Pluto" };
  } else {
    return {
      name: "Rama",
      managePeople(): void {
        console.log("Managing People...");
      },
      delegateTasks(): void {
        console.log("Delgate Tasks...");
      },
    };
  }
}

const emp: Person | DogOwner | CompManager = getEmployee();

function isManager(obj: Person | DogOwner | CompManager): obj is CompManager {
  return "managePeople" in obj;
}

if (isManager(emp)) {
  emp.delegateTasks();
} else {
  console.log("Not A Manager");
}

//Challenge 11 - Tuples and Enums

enum UserRole {
  Admin = "Admin",
  Manager = "Manager",
  Empolyee = "Empolyee",
}

type User = {
  id: number;
  name: string;
  role: UserRole;
  contact: [string, string];
};

function createUser(
  id: number,
  name: string,
  role: UserRole,
  contact: [string, string]
): User {
  return {
    id: id,
    name: name,
    role: role,
    contact: contact,
  };
}

const user1: User = createUser(1, "Umberuto", UserRole.Empolyee, [
  "Umberuto@emp.com",
  "4654645234",
]);
console.log(user1);

//Challenge 12 - Type Guarding

type valueType = string | number | boolean;

let value: valueType;
const random = Math.random();

value = random < 0.33 ? "Hello" : random > 0.66 ? 123.456 : true;

function checkValue(value: valueType) {
  if (typeof value === "string") {
    console.log(value.toLowerCase());
    return;
  } else if (typeof value === "number") {
    console.log(value.toFixed(2));
    return;
  } else {
    console.log(`boolean: ${value}`);
  }
}

checkValue(value);

type Dog = { type: "dog"; name: string; bark: () => void };
type Cat = { type: "cat"; name: string; meow: () => void };
type Animal = Dog | Cat;

function makeSound(animal: Animal): void {
  if (animal.type === "dog") {
    animal.bark();
  } else {
    animal.meow();
  }
}

function checkSound(animal: Animal) {
  if ("bark" in animal) {
    animal.bark();
  } else {
    animal.meow();
  }
}

function printLength(str: string | null | undefined): void {
  if (str) {
    console.log(str.length);
  } else console.log("No String Provided");
}

function checkInput(date: Date | string): string {
  if (date instanceof Date) {
    return date.getFullYear().toString();
  } else return date;
}

type Student = {
  name: string;
  study: () => void;
};

type Consumer = {
  name: string;
  login: () => void;
};

type Citizen = Student | Consumer;

const randomPerson = (): Citizen => {
  return Math.random() > 0.5
    ? { name: "john", study: () => console.log("Studying") }
    : { name: "mary", login: () => console.log("Logging in") };
};

const person = randomPerson();

function isStudent(person: Citizen): person is Student {
  return (person as Student).study !== undefined;
}

if (isStudent(person) === true) {
  person.study();
} else {
  console.log(person);
}


type IncrementAction = {
  type: "increment";
  amount: number;
  timestamp: number;
  user: string;
};

type DecrementAction = {
  type: "decrement";
  amount: number;
  timestamp: number;
  user: string;
};

type Action = IncrementAction | DecrementAction;

function reducer(state: number, action: Action): number {
  switch (action.type) {
    case 'increment':
      return state + action.amount;
    case 'decrement':
      return state - action.amount;
    default:
      const unexpectedActino: never = action;
      throw new Error(`Unexpected Action ${unexpectedActino}`)
  }
}

const newState = reducer(15, {
  user: "john",
  type: "increment",
  amount: 10,
  timestamp: 123456,
});
// console.log(newState);

// Challenge 12
