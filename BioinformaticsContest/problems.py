# problems.py
# Functions corresponding to questions from Bioinformatics Contest 2021
# these functions accept input data and parse it into useful test cases
# they call utility methods from helper files to solve the problems, and return each answer in an array

import utils
from pprint import pprint
from decimal import Decimal
from qualification_round.problem1 import parse_epigenomic_matrix
from qualification_round.problem2 import annotate_metabolites
from qualification_round.problem3 import build_tree, find_node_path, process_node_matrix, id_disease
from numpy import array
from tqdm import tqdm
import concurrent.futures as cf


def Welcome_1_1(lines):
    ''' demo method, sums two numbers '''
    results = []
    for line in lines:
        result = sum([int(i) for i in line.split()])
        results.append(result)
    return results

def Welcome_1_2(lines):
    ''' demo method: finds indices of substring in superstring '''
    cases = []
    for i in range(0, len(lines)):
        if i % 2 == 0:
            cases.append([lines[i], lines[i+1]])
    results = []
    for case in cases:
        results.append(utils.find_motif_indices(case[0], case[1]).strip())
    return results

def Epigenomic_Marks_2(lines):
    ''' Qualification Round Problem 1: identifies, enumerates and maps uniques states at each index of n strings '''
    cases = []
    for i in range(0, len(lines)):
        case = {}
        splitline = lines[i].split(' ')
        if len(splitline) > 1:  # test if line is start of new case
            case['n'] = int(splitline[0])   # n is number of strings in case
            case['l'] = int(splitline[1])   # l is length of all strings in case
            case['matrix'] = [line for line in lines[i+1 : i+case['n']+1]]  # save 2D array of each string in case
            cases.append(case)
    results = []
    for case in cases:
        results.append(parse_epigenomic_matrix(case))
    return results

def Metabolite_Annotation(lines):
    print('Parsing file...')
    cases = []
    for i in range(0, len(lines), 4):
        case = {}
        spec = [int(num) for num in lines[i].split(' ')]
        case['M'] = spec[0]
        case['K'] = spec[1]
        case['N'] = spec[2]
        case['m'] = [float(el) for el in lines[i+1].split(' ')]
        case['a'] = [float(el) for el in lines[i+2].split(' ')]
        case['s'] = [float(el) for el in lines[i+3].split(' ')]        
        cases.append(case)
    print('Annotating Cases...')
    results = []
    for case in cases:
        results += annotate_metabolites(case)
    return results

def Diagnosis(lines):
    print('Parsing Lines...')
    parents = [int(num) for num in lines[0].split(' ')]
    ic_content = [int(num) for num in lines[1].split(' ')]
    max_ic = max(ic_content)
    min_ic = min(ic_content)
    tree, node_map = build_tree(parents, ic_content)
    
    print('Parsing Diseases...')
    m = int(lines[2])   # num diseases
    diseases = [[int(num) for num in line.split(' ')[1:]] for line in lines[3: 3+m]]
    disease_matrix = process_node_matrix(node_map, diseases)
    
    print('Parsing Patients...')
    q = int(lines[3+m])    # num patients
    patients = [[int(num) for num in line.split(' ')[1:]] for line in lines[4+m: 4+m+q]]
    patient_matrix = process_node_matrix(node_map, patients)

    print('Diagnosing...')        
    results = []
    with tqdm(total=len(patient_matrix), desc='Diagnosing Patients: ') as pbar:
        with cf.ProcessPoolExecutor(max_workers=7) as executor:
            futures = [executor.submit(id_disease, disease_matrix, patient) for patient in patient_matrix]
            for future in cf.as_completed(futures):
                res = future.result()
                results.append(res)
                pbar.update(1)
    return results