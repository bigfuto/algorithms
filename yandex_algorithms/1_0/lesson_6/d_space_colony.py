n, a, b, w, h = map(int, input().split())

left = 0
right = min(w, h)

while left < right:
    m = (left + right + 1) // 2
    if n <= max(
            (w // (a + 2 * m)) * (h // (b + 2 * m)),
            (h // (a + 2 * m)) * (w // (b + 2 * m))
    ):
        left = m
    else:
        right = m - 1

print(left)
