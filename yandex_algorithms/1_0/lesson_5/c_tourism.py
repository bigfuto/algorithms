N = int(input())
a = int(input().split()[1])

seq = [[0] * (N + 1), [0] * (N + 1)]

for i in range(1, N):
    b = int(input().split()[1])
    if a < b:
        seq[0][i + 1], seq[1][i + 1] = seq[0][i] + b - a, seq[1][i]
    else:
        seq[1][i + 1], seq[0][i + 1] = seq[1][i] + a - b, seq[0][i]
    a = b

M = int(input())
ans = [0] * M

for i in range(M):
    a, b = map(int, input().split())
    if a < b:
        ans[i] = seq[0][b] - seq[0][a]
    else:
        ans[i] = seq[1][a] - seq[1][b]

print(*ans, sep='\n')
