async function fetchData() {


    const pokemonName = document.querySelector('#pokemonName').value.toLowerCase()

    const response =  await fetch(`https://pokeapi.co/api/v2/pokemon/${pokemonName}`);
    const data = await response.json()
    console.log(data);

    const pokemonSprite = document.querySelector("#pokemonSprite")
    pokemonSprite.src = data.

}

fetchData()