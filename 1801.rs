use std::io;
use std::cmp;

fn main(){
    let mut line = String::new();
    io::stdin().read_line(&mut line).expect("Failed to read line");

    let inputs: Vec<u32> = line.split_whitespace()
        .map(|x| x.parse::<u32>().expect("Not an integer!"))
        .collect();

    let a = inputs[0];
    let b = inputs[1];
    let c = inputs[2];

    let min_val:u32 = cmp::min(cmp::min(a,b),c);

    println!("{min_val}");


}
