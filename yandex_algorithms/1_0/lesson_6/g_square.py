n, m, t = (int(input()) for _ in range(3))

left, right = 0, min(n, m) // 2

while left < right:
    mid = (right + left + 1) // 2
    if 2 * mid * (n + m - mid * 2) <= t:
        left = mid
    else:
        right = mid - 1

print(left)
