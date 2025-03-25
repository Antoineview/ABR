# Exercice 1.2 (Utilisation)
# %% Ajout
def heap_push(H,val,elt):
    i = len(H)
    H.append(None)
    i2 = i // 2
    while (i2 > 0) and val < H[i2][0]:
        H[i] = H[i2]
        i = i2
        i2 //= 2

    H[i] = (val, elt)

H = [ None ]
heap_push(H , 8 , 'A')
print(H)
heap_push (H , 9 , 'D')
print(H)
heap_push (H , 1 , 'C')
print(H)
heap_push (H , 2 , 'B')
print(H)
# %% Suppression
def heap_pop(H):
    to_pop = H[1]
    last = H.pop()

    if len(H) > 1:
        i = 1
        size = len(H)

        while 2*i < size:
            left_child = 2*i
            right_child = 2*i + 1
            if right_child < size and H[right_child][0] < H[left_child][0]:
                smallest = right_child
            else:
                smallest = left_child
            if last[0] <= H[smallest][0]:
                size = 0
            H[i] = H[smallest]
            i = smallest
        H[i] = last

    return to_pop

# %% Mise à jour
def heap_update(H, pos, newval):
    if pos <= 0 or pos >= len(H):
        raise Exception

    oldval = H[pos][0]
    elt = H[pos][1]

    if newval < oldval:
        i = pos
        i2 = i // 2
        while i2 > 0 and newval < H[i2][0]:
            H[i] = H[i2]
            i = i2
            i2 //= 2
        H[i] = (newval, elt)
    elif newval > oldval:
        i = pos
        size = len(H)
        while 2*i < size:
            left_child = 2*i
            right_child = 2*i + 1
            if right_child < size and H[right_child][0] < H[left_child][0]:
                smallest = right_child
            else:
                smallest = left_child
            if newval <= H[smallest][0]:
                break
            H[i] = H[smallest]
            i = smallest
        H[i] = (newval, elt)
    # Si newval == oldval, on ne fait rien

H = [ None , (1 , 'D') , (8 , 'C') , (9 , 'C') , (2 , 'B') ]

heap_update(H,3,0)
print(H)

# %% Tri
def heap_sort(L):
    tas = [None]
    res = []
    for i in L :
        heap_push(tas,L[i][0],L[i][1])
    while tas != [None]:
        res.append(heap_pop(tas))
        Long -= 1
    return res

# %% heapify


