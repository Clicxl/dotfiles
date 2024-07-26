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
        const match = place.city.match(regex)|| place.state.match(regex);
        console.table(match);
        return match;
    })
}

function numberWithCommas(x) {
  return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}

function dispMatches() {
  const matchArr = findMachtes(this.value, cities)
  const html = matchArr.map(place => {
    const regex = new RegExp(this.value,'gi');
    const cityName = place.city.replace(regex,`<span class="hl">${this.value}</span>`)
    const stateName = place.state.replace(regex,`<span class="hl">${this.value}</span>`)
    return `
    <li>
    <span class='name'>${cityName}, ${stateName}</span>
    <span class='population'> ${numberWithCommas(place.population)}</span>
    </li>
    `;
  }).join("");
  suggestions.innerHTML = html;
}

const searchInput = document.querySelector(".search");
const suggestions = document.querySelector(".suggestions");

searchInput.addEventListener('change', dispMatches);
searchInput.addEventListener("keyup", dispMatches);
