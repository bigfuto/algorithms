N, x, y = map(int, input().split())

first = min(x, y)
left, right = 0, first * N

while left < right:
    m = (left + right) // 2
    if (1 + m // x + m // y) >= N:
        right = m
    else:
        left = m + 1

print(left + first)
