#![allow(unused)]
use std::io;
use rand::Rng;
use std::io::{Write, BufRead,BufReader, ErrorKind};
use std::fs::File;
use std::cmp::Ordering;

fn main() {
  let age = rand::thread_rng().gen_range(10..150);
  if (age < 13) || (age <= 18) {
    println!("{} is just a kid", age);
  } else if (age > 65) && (age <= 100)  {
    println!("{} is old age mf",age);
  } else if (18 < age) && (age <= 65) {
    println!("{} is young af",age);
  }  else{
    println!("What are you an alien? at {}",age);
  }



}