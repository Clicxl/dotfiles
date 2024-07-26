let heros = ['ironman', 'hulk','thor','spiderman','antman']

for (let i = 0 ; i <= heros.length - 1 ; i++) {
    console.log(heros[i])
}

for (let val of heros) {
    console.log(val)
}

for (let val in heros) {
    console.log(val)
}