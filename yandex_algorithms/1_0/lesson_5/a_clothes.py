N = int(input())
singlets = list(map(int, input().split()))
M = int(input())
pants = list(map(int, input().split()))

diff, singlet, trouser = 10000000, 0, 0
j = 0

for i in range(N):
    while j < M and singlets[i] > pants[j]:
        if diff > singlets[i] - pants[j]:
            diff, singlet, trouser = singlets[i] - pants[j], i, j
        j += 1
    if j == M or diff == 0:
        break
    elif diff > pants[j] - singlets[i]:
        diff, singlet, trouser = pants[j] - singlets[i], i, j

print(singlets[singlet], pants[trouser])
