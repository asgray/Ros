use std::fs;

pub fn read_file() -> String {
    let contents = fs::read_to_string("../../_input.txt")
        .expect("Reading Input failed");
    return contents
}
