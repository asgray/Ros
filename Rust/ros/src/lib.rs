use std::fs;
use std::io::{Result, Write};

pub fn read_file() -> String {
    let contents = fs::read_to_string("../../_input.txt")
        .expect("Reading Input Failed");
    return contents
}

pub fn write_file(outstr: String) -> Result<()> {
    let mut f = fs::OpenOptions::new().write(true).truncate(true).open("../../_output.txt")?;
    f.write(outstr.as_bytes())?;
    Ok(())
}