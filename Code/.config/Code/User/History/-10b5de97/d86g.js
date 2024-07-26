function alphacount(str) {
    count = 0
    for ( let val in str) {
        if (val in ['a','e','i','o','u']) {
            ++count;
        }

    }
    return count;
}

