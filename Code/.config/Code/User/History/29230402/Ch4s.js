function setDate() {
    const now = new Date();
    seconds = now.getSeconds();
    minute = now.getMinutes();
    hours = now.getHours();

    const secDeg = ((seconds / 60) * 360);
    secHand.style.

}

const secHand = document.querySelector(".second-hand")

// setInterval(setDate,1000);
