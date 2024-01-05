pub fn revc(instr: String) -> String {
   let mut rc = vec![];
   for char in instr.chars().rev() {
      let comp = match char{
         'A' => 'T',
         'T' => 'A',
         'C' => 'G',
         'G' => 'C',
         _ => panic!(),
      };
      rc.push(comp);
   }
   String::from_iter(rc)
}