from Bio.Seq import Seq
my_seq = Seq('TTGTGACGATGTCATTCGCATTACTGAGGCCCGCGGGATGTCGGCAGCCGGTGGGAGCTTAAGATCTTGTCACCGAACCTTTGGGACCTAGATGTTGGTATATACCTAGTCTGCGTGCAAGTTTCAGAGGTTGATCAGGACGGGTTGCAGGAAGTATCGCGATATAGGCACGCGAAGCTTGCCCGAGTCACATTCATGAAAACTCCGCATTCGGCTACCTGCTCAGATACATCGTAGCCCGCAGCTAAGCTCCAGGATAGCACTGCAATGAATATCCGGCGAATTTCGTACCCATCACTTCATTGCTCCGAACGTTTTCGCTGACGCAAGCTCTTCTGTCTGCGTGGGTGTCGTGTTAATCGCTCCTACTCCTGGGATGACATGACCGGAACCTGCTGGGGGCGCACACAGCCATGTGCAATGCTCGTGTCGTCAGACTCGAGCACAAATCGCTGTTAAACGAGGCACTAAGCCGGATTTTGGAATAGCAAACCTCGGCGACTAGAGGACTGAGGTACCTCTCTAGCCACGAGGACGCAGGCAAGCGGCGCCTAATCCAATCAAGTATCCCTAGCCCTATACATATGCGTAGAATGCCAGTAATGATCCTCAAGATCCTTTTTCCAGTAACAGGACGAGTACGCAATGTGTCACATCCCGAGCATTAGGCAACTAGAGAAGACGACGTGGTTAACCTAGGTACTACATCGACGGAATAGTAGTCGTACATGCAGTTGATAGAGTTAATAGGATGAACAGCTGTGGAGAGATGGGTAAGACACTGTTCAGACTGTGCGTCGGTTATGGTTTGATTAGTGTTGCTGCCCTACCAAAGGTTAATAATTGGCCCGGCTGTAAGAAGGAGTGACACCCCTTTTCTCAACGAGGTC')
print my_seq.count('A')
print my_seq.count('C')
print my_seq.count('G')
print my_seq.count('T')