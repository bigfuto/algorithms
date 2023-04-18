n, r = map(int, input().split())
seq = list(map(int, input().split()))

ans, j = 0, 1

for i in range(n):
    while j < n and seq[i] + r >= seq[j]:
        j += 1
    ans += n - j

print(ans)
