
// Get your shorts on - this is an array workout!
// ## Array Cardio Day 1

// Some data we can work with

const inventors = [
    { first: 'Albert', last: 'Einstein', year: 1879, passed: 1955 },
    { first: 'Isaac', last: 'Newton', year: 1643, passed: 1727 },
    { first: 'Galileo', last: 'Galilei', year: 1564, passed: 1642 },
    { first: 'Marie', last: 'Curie', year: 1867, passed: 1934 },
    { first: 'Johannes', last: 'Kepler', year: 1571, passed: 1630 },
    { first: 'Nicolaus', last: 'Copernicus', year: 1473, passed: 1543 },
    { first: 'Max', last: 'Planck', year: 1858, passed: 1947 },
    { first: 'Katherine', last: 'Blodgett', year: 1898, passed: 1979 },
    { first: 'Ada', last: 'Lovelace', year: 1815, passed: 1852 },
    { first: 'Sarah E.', last: 'Goode', year: 1855, passed: 1905 },
    { first: 'Lise', last: 'Meitner', year: 1878, passed: 1968 },
    { first: 'Hanna', last: 'Hammarström', year: 1829, passed: 1909 }
];

const people = [
    'Bernhard, Sandra', 'Bethea, Erin', 'Becker, Carl', 'Bentsen, Lloyd', 'Beckett, Samuel', 'Blake, William', 'Berger, Ric', 'Beddoes, Mick', 'Beethoven, Ludwig',
    'Belloc, Hilaire', 'Begin, Menachem', 'Bellow, Saul', 'Benchley, Robert', 'Blair, Robert', 'Benenson, Peter', 'Benjamin, Walter', 'Berlin, Irving',
    'Benn, Tony', 'Benson, Leana', 'Bent, Silas', 'Berle, Milton', 'Berry, Halle', 'Biko, Steve', 'Beck, Glenn', 'Bergman, Ingmar', 'Black, Elk', 'Berio, Luciano',
    'Berne, Eric', 'Berra, Yogi', 'Berry, Wendell', 'Bevan, Aneurin', 'Ben-Gurion, David', 'Bevel, Ken', 'Biden, Joseph', 'Bennington, Chester', 'Bierce, Ambrose',
    'Billings, Josh', 'Birrell, Augustine', 'Blair, Tony', 'Beecher, Henry', 'Biondo, Frank'
];

// Array.prototype.filter()
// 1. Filter the list of inventors for those who were born in the 1500's
let yearFil = []
inventors.forEach((obj) => {
    if (obj.year >= 1500 && obj.year <= 1600){
        yearFil.push(obj);
    }
    })

// console.table(yearFil);

let filMeth = inventors.filter((obj) => obj.year >= 1500 && obj.year <= 1600)
console.table(filMeth)

// -------------------------------------------------------------------------------------------------------

// Array.prototype.map()
// 2. Give us an array of the inventors first and last names
let fullName = []
inventors.forEach((obj) => {
    fullName.push(`${obj.first} ${obj.last}`);
})
// console.log(fullName)

const fullNames = inventors.map(obj => `${obj.first} ${obj.last}`)
console.log(fullNames);

// -------------------------------------------------------------------------------------------------------

// Array.prototype.sort()
// 3. Sort the inventors by birthdate, oldest to youngest
let ageSort = inventors.sort((firstObj,secObject) => {
    return firstObj.year - secObject.year // If the returned number is negative then the sort method will push it down the array
})

ageSort = inventors.sort((a,b) => a.year > b.year ? 1 : -1)
console.table(ageSort);

// -------------------------------------------------------------------------------------------------------

// Array.prototype.reduce()
// 4. How many years did all the inventors live all together?

const redcued = inventors.reduce((total,obj) => {
    return total + (obj.passed - obj.year)},0) // first time the total is not defined so it shows reduced as an object something but the 0 delimitor start total from 0

console.log(redcued);

// -------------------------------------------------------------------------------------------------------

// 5. Sort the inventors by years lived
const sortYear = inventors.sort((a,b) => (a.passed - a.year) > (b.passed - b.year) ? 1 : -1).reverse()
console.table(sortYear);

// 6. create a list of Boulevards in Paris that contain 'de' anywhere in the name
// https://en.wikipedia.org/wiki/Category:Boulevards_in_Paris
// const category = document.querySelector(".mw-category");
// const links = [...category.querySelectorAll("a")]; // [...] spreads the array
// const de = links
//                 .map((link) => link.textContent)
//                 .filter(streetName => streetName.includes("de"))

// -------------------------------------------------------------------------------------------------------

// 7. sort Exercise
// Sort the people alphabetically by last name
const sortPeople = people.sort((a,b) => {
    const aSplit = a.split(", ")
    const bsplit = b.split(", ")
    return a[1] > b[1] ? 1 : -1
})
console.table(sortPeople)

// -------------------------------------------------------------------------------------------------------

// 8. Reduce Exercise
// Sum up the instances of each of these
const data = ['car', 'car', 'truck', 'truck', 'bike', 'walk', 'car', 'van', 'bike', 'walk', 'car', 'van', 'car', 'truck' ];
