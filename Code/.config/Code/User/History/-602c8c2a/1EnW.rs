#![allow(unused)]
use std::io;
use rand::Rng;
use std::io::{Write, BufRead,BufReader, ErrorKind};
use std::fs::File;
use std::cmp::Ordering;


/* use - this is like import in python and "::" is used a from <> import */

/*  fn - is a function definer just like def
"main" - is the main function which runs all the code */

/*
fn main() {
    println!("Hello, world!");
} */

/*  Cargo.toml - for depencies
    Cargo manages all the depencies
    cargo build- Build the exe files to runable (Stored in : target/debug)
    cargo run- Run the exe files
    cargo check - Check for errors in the app
*/

/*   rustfmt - Formats tge file in a proper manner*/

/// Variables
fn main() {
    /*  let x = 4;

    // You cannot change the vaules of a varible like in python
    x = 5;

    println!("x is: {}", x); // This "{}",<value> is like formating string in python */

    /*  let mut y = 10;
    // warning: value assigned to `y` is never read : this is beacuse y is not used anywhere - can be ignored for now
    y = 17;
    println!("y is changed: {}", y); */

    /*  // This can be done in rust - Redeclation of variables
    let z = 15;
    println!("z is : {}", z);
    let z = z + 5;
    println!("z is changed to: {}", z); */

/*  // Name Shadowing
    let x = 4;
    println!("x is : {}", x);

    {
        // Creates a local variable that can be used inside only in {}
        // the x from the global can be used inside this scope
        let x = x - 2;
        println!("x is: {}", x);
    }

    let x = x + 5;
    println!("x is: {}", x);

    /*  // Constants
    const SECONDS_IN_MINUTE: u32 = 60;
    // Cannot redefine a constant like variable
    println!("{}",SECONDS_IN_MINUTE) */

    // Primitive Datatypes -
    // Scalar Type - ints , bools ect
    let x: i32 = 2; // "i32" - integer of 32 bits: "i32" is a scalar datatype
                    // other examples of intergers are: i8 i16 i32 i64 i128
                    // i - signed integer, number whose sign can be changed: x:i32 = -654 is possible

    let x: u32 = 54;
    // u - unsigned integer, number whose sign cannot be changed: x:u32 = -345 is not possible

    // Floats - f32 f64
    let single_precision: f32 = 15.7;

    // Boolean
    let t_or_f: bool = false; // 0 and 1 can also be used

    // Character - char
    let letter: char = '4';

    // Compound Types:
    // Tuples
    let tup1: (i32, bool, char) = (1, true, 'a');
    // tup1 != tup2 - because i32 != i8
    println!("{}", tup1.2); // tuple.<index> : to access the values of tuples

    let mut tup2: (i64, bool, char) = (1, true, 'a');
    tup2.0 = 10;
    println!("{}", tup2.0); */

/*  //Arrays
    let mut arr = [1,2,3,4,5];
    arr[0] = 6;
    println!("{}",arr[0]); */

    // String

    let x: u32 = 15;
    let y = x;
    println!("{},{}",x,y);

/*  // Input From User
    println!("What is your Name?");
    let mut name: String= String::new();
    // String::new() - reutrns a new string
    let greeting: &str = "Nice to Meet you";
    io::stdin().read_line(&mut name)// This is the way to take user input using the io crate
        .expect("Didnt Receive an Input");
    println!("Hello {}! {}", name.trim_end(),greeting); */



}
