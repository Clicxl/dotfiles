function alphacount(str) {
    count = 0
    for ( let char in str) {
        if (char) {
            ++count;
        }

    }
    return count;
}

