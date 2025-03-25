# %% Exercice 1 : Recherches

# 1.1

def minBst(B):
    if B.left == None:
        return B.key
    else :
        return minBst(B.left)
