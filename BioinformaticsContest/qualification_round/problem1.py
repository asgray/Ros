# Problem 1: Epigenomic Markers
def parse_epigenomic_matrix(case):
    ''' function accepts a 2D array, or array of strings with length l '''
    l = case['l']
    matrix = case['matrix']
    state_list = []     # save each column, or state, in order
    for i in range(0, l):
        state = ''
        for line in matrix:
            state += line[i]
        state_list.append(state)
    state_set = set(state_list)     # extract unique states
    state_key = dict(zip(state_set, range(1, len(state_set)+1))) # assign each unique state a number  ** order is arbitrary **
    state_map = ''
    for state in state_list:        # map each state number to each of l indices for each state in the test case
        state_map += str(state_key[state]) + ' '
    return f'{str(len(state_set))}\n{state_map.strip()}'    # return string