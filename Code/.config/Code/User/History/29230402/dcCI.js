function setDate() {
    const now = new Date();
    seconds = now.getSeconds();
    minute = now.getMinutes();
    hours = now.getHours();

    trfDeg(seconds,secHand);
    trfDeg(minute,minHand);
    trfDeg(hour,hoursHand);

}

const secHand = document.querySelector(".second-hand")
const minHand = document.querySelector(".minute-hand");
const hoursHand = document.querySelector(".hour-hand");



function trfDeg(time,styleClass) {
    const secDeg = (time / 60) * 360;
    styleClass.style.transform = `rotate(${secDeg}deg)`;

}

setInterval(setDate,1000);
