function alphaCount(str) {
  count = 0;
  for (let char of str) {
    if (
      char === "a" ||
      char === "e" ||
      char === "o" ||
      char === "u" ||
      char === "i"
    ) {
      count++;
    }
  }
  return count;
}


const countVowels = (str) => {
    count = 0;
    for (let char of str) {
    if (
        char === "a" ||
        char === "e" ||
        char === "o" ||
        char === "u" ||
        char === "i"
    ) {
        count++;
    }
    }
    return count;
}