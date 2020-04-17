# Given: A collection of n (n≤10) GenBank entry IDs.
# Return: The shortest of the strings associated with the IDs in FASTA format.

from Bio import Entrez
from Bio import SeqIO
Entrez.email = "your_name@your_mail_server.com"

target_ids = 'JX462670 JQ712977 JQ011270 NM_013179 NM_001133698 NM_002037 JF927157 JX398977 NM_001081821'
target_ids = target_ids.split(' ')

handle = Entrez.efetch(db="nucleotide", id=target_ids, rettype="fasta")
records = list(SeqIO.parse(handle, "fasta")) #we get the list of SeqIO objects in FASTA format

short_seq = records[0]
for rec in records:
    if len(rec) < len(short_seq):
        short_seq = rec

print(short_seq.format('fasta'))
