N = int(input())
seq = list(map(int, input().split()))
x = int(input())

diff = abs(x - seq[0])
ans = seq[0]

for i in range(1, N):
    if abs(x - seq[i]) < diff:
        diff = abs(x - seq[i])
        ans = seq[i]

print(ans)
