async function fetchData() {

    const response =  await fetch("https://pokeapi.co/api/v2/pokemon/pikachu");
    const data = await response.json()
    console.log(data);

}

fetchData()