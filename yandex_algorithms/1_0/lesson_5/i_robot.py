K = int(input())
line = input()

ans, now = 0, 0

for i in range(K, len(line)):
    now = now + 1 if line[i] == line[i - K] else 0
    ans += now

print(ans)
