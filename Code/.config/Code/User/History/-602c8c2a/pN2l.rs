#![allow(unused)]
use std::io;
use rand::Rng;
use std::io::{Write, BufRead,BufReader, ErrorKind};
use std::fs::File;
use std::cmp::Ordering;

fn main() {
    let mut my_age = rand::thread_rng().gen_range(1..101);
    let voting = if (my_age >= 18) {
      true
    } else { false };
    println!("{}",voting);
}