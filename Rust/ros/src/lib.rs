use std::error::Error;
use std::fs;

pub fn run(config: Config) -> Result<(), Box<dyn Error>>{
    let input = fs::read_to_string(config.in_file)?;

    println!("Command: {}", config.command);
    println!("Input:\n{input}");

    Ok(())
}

pub struct Config {
    pub command: String,
    pub in_file: String
}

impl Config {
    pub fn build(args: &[String]) -> Result<Config, &'static str> {
        if args.len() < 3 {
            return Err("not enough arguments");
        }

        let command = args[1].clone();
        let in_file = args[2].clone();
        
        Ok(Config {command, in_file})
    }
}