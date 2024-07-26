const endPoint =
    "https://gist.githubusercontent.com/Miserlou/c5cd8364bf9b2420bb29/raw/2bf258763cdddd704f8ffd3ea9a3e81d25e2c6f6/cities.json";


const cities = [];

fetch(endPoint)
    .then((blob) => blob.json())
    .then(data => cities.push(...data));

function findMachtes(wordInput, cities) {
    return cities.filter(place => {
    // if (place.city.includes(wordInput)) {
		// 			console.log(place);
		// 		}
        const regex = new RegExp(wordInput,'gi')
        return place.city.match(regex) || place.state.match(regex);
    })
}

function dispMatches() {
  const matchArr = findMachtes(this.value, cities)
}

const searchInput = document.querySelector(".search");
const suggestions = document.querySelector(".suggestions");

searchInput.addEventListener('change', dispMatches);
searchInput.addEventListener("keyup", dispMatches);
