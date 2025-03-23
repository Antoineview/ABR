# Exercice 1
def detect_neg(M):
    l,c = len(M),len(M[0])
    i = 0
    j = c
    while i<l and j == c:
        j = 0
        while j < c and M[i][j] >= 0:
            j += 1
        i += 1
    return j < c

# Exercice 2

def build_symetric(M):
    (lig,col) = (len(M),len(M[0]))
    R = []
    for _ in range(2*lig):
        L = []
        for _ in range(col):
            L.append(0)
        R.append(L)
    for i in range(lig):
        for j in range(col):
            R[i][j] = M[i][j]
            R[2*lig-i-1][j] = M[i][j]
    return R
