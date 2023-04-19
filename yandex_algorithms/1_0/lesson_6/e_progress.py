a, b, c = (int(input()) for _ in range(3))

count = a + b + c
total = (a * 2 + b * 3 + c * 4) * 2
left, right = 0, count

while left < right:
    m = (left + right) // 2
    if (m * 10 + total) // (count + m) >= 7:
        right = m
    else:
        left = m + 1

print(left)
