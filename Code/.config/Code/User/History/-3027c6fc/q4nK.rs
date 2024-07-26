fn main() {

    let x:i32 = 10;

    {
        let y:i32 = 5;
        println!("The Value of x is {} and the vaule of y is {}",x,y);
    }

    println!("The Value of x is {}",x);

}