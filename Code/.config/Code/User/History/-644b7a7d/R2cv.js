async function fetchData() {


    const pokemonName = document.querySelector('#pokemonName').value.toLower()

    const response =  await fetch("https://pokeapi.co/api/v2/pokemon/pikachu");
    const data = await response.json()

}

fetchData()