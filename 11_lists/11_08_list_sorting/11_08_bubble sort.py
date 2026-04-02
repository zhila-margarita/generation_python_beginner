#сортировка пузырьком, повторение

seq = [5,-7,9,12,-4,0]

n = len(seq)

for i in range (n-1):
    flag = True
    for j in range (0, n-1-i):
        if seq[j]<seq[j+1]:
            seq[j], seq[j+1] = seq[j+1], seq[j]
            flag = False
            
    if flag:
        break
print(seq)