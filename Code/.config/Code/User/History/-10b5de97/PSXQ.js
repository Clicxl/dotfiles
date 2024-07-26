function alphacount(str) {
    count = 0
    for ( let char in str) {
        if (char === 'a' || char === 'e' || char === 'o' || char === 'u') {
            ++count;
        }

    }
    return count;
}

