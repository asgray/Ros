# Given: A genus name, followed by two dates in YYYY/M/D format.
# Return: The number of Nucleotide GenBank entries for the given genus that were published between the dates specified.

from Bio import Entrez

Entrez.email = 'tonysgray@gmail.com'

genus = 'Hulodes'
start = '2008/07/11'
end = '2011/08/05'
handle = Entrez.esearch(db="nucleotide", term=f'{genus}[Organism] AND {start}:{end}[dp]')
record = Entrez.read(handle)

print(record['Count'])