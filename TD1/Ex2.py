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
                break
            H[i] = H[smallest]
            i = smallest
        H[i] = last

    return to_pop

H = [None, (1, 'C'), (2, 'B'), (8, 'A'), (9, 'D')]
print(heap_pop(H))
print(H)
print(heap_pop(H))
print(H)
print(heap_pop(H))
print(H)
print(heap_pop(H))
print(H)
