w, h, n = map(int, input().split())

left = 0
right = (w + h) * n + 10

while left < right:
    m = (left + right) // 2
    width_amount = m // w
    height_amount = m // h
    if n <= width_amount * height_amount:
        right = m
    else:
        left = m + 1

print(left)
