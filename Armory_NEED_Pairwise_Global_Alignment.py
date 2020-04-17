# Given: Two GenBank IDs.
# Return: The maximum global alignment score between the DNA strings associated with these IDs.
# outputs are copied into Needle inputs at http://www.bioinformatics.nl/emboss-explorer/
# Gap opening penalty was 10, gap extension was 1, end gap penalties applied

file = None
with open('input.txt', 'r') as f:
    file = f.read()
    print('Inputs Read')

from Bio import Entrez
from Bio import SeqIO
Entrez.email = "your_name@your_mail_server.com"

target_ids = file.split(' ')

handle = Entrez.efetch(db="nucleotide", id=target_ids, rettype="fasta")
records = list(SeqIO.parse(handle, "fasta")) 

out = ''
for rec in records:
    out += rec.format('fasta')+'\n'

with open('output.txt', 'w') as f:
    f.write(out)
    print('Outputs Saved')