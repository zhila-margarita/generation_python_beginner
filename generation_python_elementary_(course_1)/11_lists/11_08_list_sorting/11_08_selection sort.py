#сортировка выбором, повторение

seq = [5,-7,9,12,-4,0]

n = len(seq)

for i in range (n-1):
    min_ind = i
    for j in range (i, n):
        if seq[j]<seq[min_ind]:
            min_ind =j
        
    seq[i],seq[min_ind] = seq[min_ind], seq[i]
        
print(seq)