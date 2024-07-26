#![allow(unused)]
use std::io;
use rand::Rng;
use std::io::{Write, BufRead,BufReader, ErrorKind};
use std::fs::File;
use std::cmp::Ordering;

fn main() {
  let age = rand::thread_rng().gen_range(10..80);
  if (age < 13) {
    println!("{} is just a kid", age);
  } else if (age > 65) {
    println!("{} is old age mf",age);
  } else if (13 < age < 65 ) {
    


  }  else{
    println!("What are you an alien?");
  }



}