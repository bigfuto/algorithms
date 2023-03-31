seq = list(map(int, input().split()))
ans = 'YES'

for i in range(len(seq) - 1):
    if seq[i] >= seq[i + 1]:
        ans = 'NO'
        break

print(ans)
