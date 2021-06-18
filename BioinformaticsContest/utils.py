#utils.py
# utility for Bioinformatics Contest 2021

# I/O ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def load_input(filepath):
    with open(filepath, 'r') as file:
        lines = [line.strip() for line in file]
        cases = lines.pop(0)
        return cases, lines

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

# def solveable_f(symbol_list, str_expr):
#     return lambdify(symbols(symbol_list), sympify(str_expr), 'math')