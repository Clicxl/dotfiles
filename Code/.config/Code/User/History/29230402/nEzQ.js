function setDate() {
    const now = new Date()
    seconds = now.getSeconds()
    minute = now.getMinutes()
    hours = now.getHours()

    console.log(seconds,minute,hours);
}

setInterval(setDate,1000);