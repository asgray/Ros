#utils.py
# utility for Bioinformatics Contest 2021
from tqdm import tqdm
import concurrent.futures as cf

# I/O ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def load_input(filepath):
    with open(filepath, 'r') as file:
        lines = [line.strip() for line in file]
        # cases = lines.pop(0)
        return lines

def save_output(filepath, results):
    with open(filepath, 'w') as file:
        for result in results:
            file.write(str(result) + '\n')
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Intro ---------------------------------------------
def find_motif_indices(s,t):
    indexes = ''
    for i in range(0, len(s)-len(t)+1):
        substr = s[i: i+len(t)]
        if substr == t:
            indexes += str(i+1)+' '
    return indexes
# ---------------------------------------------------

# def multiprocess(func, total, desc, args, item_list):
#     results = []
#     with tqdm(total=total, desc=desc) as pbar:
#         with cf.ProcessPoolExecutor(max_workers=7) as executor:
#             futures = [executor.submit(func, args) for item in item_list]
#             for future in cf.as_completed(futures):
#                 res = future.result()
#                 results.append(res)
#                 pbar.update(1)

# def solveable_f(symbol_list, str_expr):
#     return lambdify(symbols(symbol_list), sympify(str_expr), 'math')