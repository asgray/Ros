use clap::Parser;

use ros::{read_file, write_file, read_fasta};
use crate::problems::dna::dna;
use crate::problems::rna::rna;
use crate::problems::revc::revc;
use crate::problems::gc::gc;

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
    println!("Command: {}", command);
    let output: String = match command.as_str() {
        "DNA"  => dna(read_file()),
        "RNA"  => rna(read_file()),
        "REVC" => revc(read_file()),
        "GC"   => gc(read_fasta()),
        _ =>  {
            println!("Unknown Command: {}", command);
            return
        },
    };
    
    write_file(output).unwrap();
}