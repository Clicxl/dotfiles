function setDate() {
    const now = new Date();
    seconds = now.getSeconds();
    minute = now.getMinutes();
    hours = now.getHours();

    trfDeg(seconds,secHand,60);
    trfDeg(minute,minHand,60);
    trfDeg(hours,hoursHand,12);
    console.log(sec);

}

const secHand = document.querySelector(".second-hand")
const minHand = document.querySelector(".minute-hand");
const hoursHand = document.querySelector(".hour-hand");



function trfDeg(time,styleClass,parts) {
    const deg = ((time / parts) * 360) + 90;
    styleClass.style.transform = `rotate(${deg}deg)`;

}

setInterval(setDate,1000);
