def subList(x, y):
    """returns list of longest common substring"""
    def findPath(mat, x, y):
        """given a Needleman-Wunsch matrix, find the longest subsequence by backtracing the path"""
        # VERY NAIVE BACK SORT. ROOM FOR IMPROVEMENT, only gives one possivle subsequence
        tempSub = ''
        row = len(y) - 1
        space = len(x) - 1
        while row > 0 and space > 0:
            if mat[row][space] == mat[row - 1][space - 1] + 1 and y[row] == x[space]:  # if number resulted in match,
                tempSub = x[space] + tempSub  # record match, move diagonal
                row -= 1
                space -= 1
            else:  # if number generated from greatest
                if mat[row][space] == mat[row - 1][space]:  # choice, backtrack to choice
                    row -= 1
                if mat[row][space] == mat[row][space - 1]:
                    space -= 1
        return tempSub
    def buildMatrix(x, y):
        """accepts 2 strings, builds an empty matrix with each as axes"""

        # ---------------------------------------------------------------------------
        def fillMatrix(mat):
            """populate matrix based on Needleman-Wunsch"""
            for row in range(1, len(y)):
                for space in range(1, len(x)):  # counts start at 1 to maintain 0s around matrix for algorithm
                    if x[space] == y[row]:  # if match is found
                        mat[row][space] = mat[row - 1][space - 1] + 1  # space = diagnal top left + 1
                    else:  # if match is not found
                        mat[row][space] = max(mat[row - 1][space], mat[row][
                            space - 1])  # space = greatest of position to left and position above
            return mat

        # ----------------------------------------------------------------------------
        matNW = []
        for ch in range(len(y)):
            matNW.append([0])
            for c in range(len(x) - 1):  # len(x)-1 because one position is made by y loop
                matNW[ch].append(0)
        fillMatrix(matNW)
        return matNW
    s = '.' + x
    t = ',' + y
    matrix = buildMatrix(s, t)
    subSeq = findPath(matrix, s, t)
    return subSeq
def splitStr(subs, dna):
    """breaks string at points in subsequence"""
    frags = []
    for char in subs:
        loc = dna.find(char)
        frags.append(dna[: loc])
        dna = dna[loc+1:]
    frags.append(dna)
    return frags
def assembleFrags(subseq, split1, split2):
    """assembles shortest common supersequence"""
    supSeq = ''
    for char in subseq:
        frag = split1[0] + split2[0] + char
        supSeq += frag
        split1 = split1[1:]
        split2 = split2[1:]
    supSeq += split1[0] + split2[0]
    return supSeq

s = 'GTAACGATATTTGATCTATGTCGTCGTCTTATTGATAGACACCTCATCCTTAGCAACCCTGCATATCTACCCCAATGCCTGACTC'                  # punctuation to build in != 0 rows to matrix
t = 'CACAAGACTATATAGGGGAAAGACTCGGAGGAATAGCAGCCATTTAAGCAGTTCTCGTGAAGCTGGAGTCAGGTTCGCGGCTTTTTATAGTGATC'
subChars = subList(s,t)
print assembleFrags(subChars, splitStr(subChars, s), splitStr(subChars, t))