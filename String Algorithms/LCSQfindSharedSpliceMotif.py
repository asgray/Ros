# USES MODIFIED NEEDLEMAN-WUNSCH ALGORITHM
#-------------------------------------------------------------------------
def importFASTA(data):
    """reads FASTA file, builds list of DNA strings"""
    dnaStrings = []
    dataset = open(data)
    appended = False
    for line in dataset:
        if line.startswith('>'):
            appended = False
        else:
            if appended is False:
                dnaStrings.append(line.strip())
                appended = True
            else:
                dnaStrings[len(dnaStrings)-1] += line.strip()
    dataset.close()
    return dnaStrings
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
def buildMatrix(x,y):
    """accepts 2 strings, builds an empty matrix with each as axes"""
    # ---------------------------------------------------------------------------
    def fillMatrix(mat):
        """populate matrix based on Needleman-Wunsch"""
        for row in range(1, len(y)):
            for space in range(1, len(x)):  # counts start at 1 to maintain 0s around matrix for algorithm
                if x[space] == y[row]:  # if match is found
                    mat[row][space] = mat[row - 1][space - 1] + 1 # space = diagnal top left + 1
                else:  # if match is not found
                    mat[row][space] = max(mat[row - 1][space], mat[row][space - 1]) # space = greatest of position to left and position above
        return mat
    # ----------------------------------------------------------------------------
    matNW = []
    for ch in range(len(y)):
        matNW.append([0])
        for c in range(len(x)-1):       # len(x)-1 because one position is made by y loop
            matNW[ch].append(0)
    fillMatrix(matNW)
    return matNW
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
def findPath(mat, x, y):
    """given a Needleman-Wunsch matrix, find the longest subsequence by backtracing the path"""
    # VERY NAIVE BACK SORT. ROOM FOR IMPROVEMENT, only gives one possivle subsequence
    tempSub = ''
    row = len(y)-1
    space = len(x)-1
    while row > 0 and space > 0:
        if mat[row][space] == mat[row-1][space-1] + 1 and y[row] == x[space]:   # if number resulted in match,
            tempSub = x[space] + tempSub                                        # record match, move diagonal
            row -= 1
            space -= 1
        else:                                                                   # if number generated from greatest
            if mat[row][space] == mat[row - 1][space]:                          # choice, backtrack to choice
                row -= 1
            if mat[row][space] == mat[row][space-1]:
                space -= 1
    return tempSub
#----------------------------------------------------------------------------
# -----for visualizing matrix----
def printMatrix(mat, x, y):
    """ prints matrix"""
    prd1 = ' '
    for char in x:
        prd1 += '  ' + char
    print prd1
    for i in range(len(mat)):
        print y[i], mat[i]
#--------------------------------

dstrs = importFASTA('input.txt')
d1 = '.'+ dstrs[0]                  # punctuation to build in != 0 rows to matrix
d2 = ','+ dstrs[1]
matrix = buildMatrix(d1, d2)
printMatrix(matrix, d1, d2)
print findPath(matrix, d1, d2)
print len(findPath(matrix, d1, d2))