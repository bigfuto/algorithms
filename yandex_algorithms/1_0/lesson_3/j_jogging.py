t, d, n = map(int, input().split())
dots = [0, 0, 0, 0]
ans = []

for _ in range(n):
    dots = [dots[0] - t, dots[1] + t, dots[2] - t, dots[3] + t]
    x, y = map(int, input().split())
    dots = [max(dots[0], x + y - d), min(dots[1], x + y + d), max(dots[2], x - y - d), min(dots[3], x - y + d)]

for plus in range(dots[0], dots[1] + 1):
    for minus in range(dots[2], dots[3] + 1):
        if (plus + minus) % 2 == 0:
            x = (plus + minus) // 2
            y = plus - x
            ans.append((x, y))

print(len(ans))
for x, y in ans:
    print(x, y)
