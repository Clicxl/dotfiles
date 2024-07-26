#![allow(unused)]
use rand::Rng;
use std::cmp::Ordering;
use std::fs::File;
use std::io;
use std::io::{BufRead, BufReader, ErrorKind, Write};

fn main() {
    let mut my_age = String::new();
    println!("Enter Your Age: ");
    my_age = io::stdin().()
    let voting = if (my_age >= 18) { true } else { false };
    println!("Age: {1} ; Can Vote: {0}", voting, my_age);
}