class Car {
    start() {
        console.log("Start");
    }

    stop() {
        console.log("Stop");
    }

    setBrand(brand) {
        this.brandName = brand;
    }
}

let fortuner = new Car();
fortuner.setBrand();