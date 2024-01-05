pub fn dna(instr: String) -> String {
    let (mut a, mut t, mut c, mut g) = (0,0,0,0);

    for char in instr.chars(){
        if char== 'A' {
            a += 1
        } else
        if char== 'C' {
            c += 1
        } else
        if char== 'T' {
            t += 1
        } else
        if char== 'G' {
            g += 1
        } 
    }

    format!("{} {} {} {}", a , c, g, t)
}