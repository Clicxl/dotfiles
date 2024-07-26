function setDate() {
    const now = new Date();
    seconds = now.getSeconds();
    minute = now.getMinutes();
    hours = now.getHours();

    const secDeg = ((seconds / 60) * 360);

}

const secHand = document.querySelector(".seconds-hand")

// setInterval(setDate,1000);
