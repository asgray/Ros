use std::fs::{read_to_string, OpenOptions, File};
use std::io::{Result, Write, BufReader, BufRead, Lines};
use std::path::Path;
use std::collections::BTreeMap;

pub fn read_file() -> String {
    let contents = read_to_string("../../_input.txt")
        .expect("Reading Input Failed");
    return contents.trim().to_string();
}

pub fn write_file(outstr: String) -> Result<()> {
    let mut f = OpenOptions::new().write(true).truncate(true).open("../../_output.txt")?;
    f.write(outstr.as_bytes())?;
    Ok(())
}

fn read_lines<P>(filename: P) -> Result<Lines<BufReader<File>>> 
where P: AsRef<Path>,{
    let file = File::open(filename)?;
    Ok(BufReader::new(file).lines())
}

pub fn read_fasta() -> BTreeMap<String, String> {
    let mut seqs = BTreeMap::new();
    let (mut id, mut seq) = (String::new(), String::new());
    if let Ok(lines) = read_lines("../../_input.txt") {
        for line in lines.flatten(){
            if line.starts_with(">"){
                if !id.is_empty(){
                    seqs.insert(id, seq);
                    seq = "".to_string();
                }
                id = line
            } else {
                seq = format!("{}{}", seq, line);
            }
        }
        seqs.insert(id, seq);
    }

    return seqs
}