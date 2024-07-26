async function fetchData() {

    const respnse = await fetch("https://pokeapi.co/api/v2/pokemon/pikachu")
    .then(response => console.log(respnse));


}

fetchData()