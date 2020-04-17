# Given: Two DNA strings s and t in FASTA format that share some short inexact repeat r of 32-40 bp. 
# By "inexact" we mean that r may appear with slight modifications (each repeat differ by ≤3 changes/indels).
#
# Return: The total number of occurrences of r as a substring of s, followed by the total number of occurrences of r as a substring of t.
#
# used https://www.ebi.ac.uk/Tools/psa/lalign/ to run Lalign
from _ros_utils import indata, outdata

dat = indata()


outdata(dat)