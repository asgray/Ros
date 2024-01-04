# Given: Two DNA strings s and t in FASTA format that share some short inexact repeat r of 32-40 bp. 
# By "inexact" we mean that r may appear with slight modifications (each repeat differ by ≤3 changes/indels).
#
# Return: The total number of occurrences of r as a substring of s, followed by the total number of occurrences of r as a substring of t.
#
# used https://www.ebi.ac.uk/Tools/psa/lalign/ to run Lalign
# run the job, then paste the View Alignment File url into _input.txt

#*** ENDED UP JUST SOLVING THE PROBLEM VISUALLY WITH BLAST

# from _ros_utils import indata, outdata, hamming_dist
# import urllib3
# from pprint import pprint
# import re
# from Bio import SeqIO

# def count_partial_aligns(seq, target, max_mismatch):
#     windowsize = len(target)
#     hits = 0
#     for i in range(len(seq)-windowsize+1):
#         substr = seq[i:i+windowsize]
#         if hamming_dist(substr, target) < max_mismatch:
#             hits += 1
#     return hits

# dat = indata()
# seqs = {}
# curline = None
# for line in dat.split('\n'):
#     if line.startswith('>'):
#         seqs[line] = ''
#         curline = line
#     else:
#         seqs[curline] += line

# s = seqs.pop('>align')
# print(len(s))
# # http = urllib3.PoolManager()
# # res = http.request('GET', url)
# # match = re.findall('(\(100\.0% similar\))((.|\n)+?)([GATC]+)',str(res.data))
# # s = re.findall('[GATC]+', str(match[0]))[0]
# # s = seqs[-1]
# out = []
# for seq in seqs:

#     out.append(count_partial_aligns(seqs[seq], s, 3))
# print(out)
# # outdata(str(out))