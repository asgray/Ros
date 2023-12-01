use std::env;
use std::fs;

fn main() {
    let args: Vec<String> = env::args().collect();
    dbg!(args);

    let input = fs::read_to_string("../../../../_input.txt")
        .expect("Couldn't Read File");

    println!("Input:\n{input}");
}
