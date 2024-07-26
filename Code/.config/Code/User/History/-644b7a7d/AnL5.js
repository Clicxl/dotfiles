async function fetchData() {


    const pokemonName = document.querySelector('#pokemonName').value.toLowerCase()

    const response =  await fetch(`https://pokeapi.co/api/v2/pokemon/${pokemonName}`);
    const data = await response.json()

    const pokemonSprite = document.querySelector()

}

fetchData()