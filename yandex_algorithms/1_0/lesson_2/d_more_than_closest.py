seq = list(map(int, input().split()))

j = 0

for i in range(1,  len(seq) - 1):
    if seq[i - 1] < seq[i] and seq[i] > seq[i + 1]:
        j += 1

print(j)
