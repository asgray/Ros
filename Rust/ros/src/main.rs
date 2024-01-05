use clap::Parser;

use ros::{read_file, write_file};
use crate::problems::dna::dna;
use crate::problems::rna::rna;
use crate::problems::revc::revc;

pub mod problems;

#[derive(Parser)]
#[command(name = "Ros")]
#[command(author = "AG")]
#[command(version = "1.0")]
#[command(about = "Ros, but in Rust", long_about = None)]
struct Cli {
    #[arg(long)]
    command: String,
}

fn main() {
    let cli = Cli::parse();
    let command = cli.command;
    let input = read_file();
    let output: String;
    println!("Command: {}", command);
    output = match command.as_str() {
        "DNA" => dna(input),
        "RNA" => rna(input),
        "REVC"=> revc(input),
        _ =>  {
            println!("Unknown Command: {}", command);
            return
        },
    };
    
    write_file(output).unwrap();
}