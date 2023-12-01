# SwissProt.read(broken)
from Bio import ExPASy
from Bio import SwissProt

def get_go_process(uniprot):
    """Function to extract GO terms for biological processes"""
    handle = ExPASy.get_sprot_raw(uniprot)
    record = SwissProt.read(handle)

    go_terms = [cross for cross in record.cross_references if 'GO' in cross]
    go_proc = []

    for term in go_terms:
        for annot in term:
            if any('P:' in annot[0:2]):
                go_proc.append(annot[2:])

    return go_proc

protein = 'B5ZC00'
go_procs = get_go_process(protein)
for p in go_procs:
    print(p)