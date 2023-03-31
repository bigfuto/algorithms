a, b, n, m = (int(input()) for _ in range(4))

first = [n + (n + i) * a for i in range(-1, 2, 2)]
second = [m + (m + i) * b for i in range(-1, 2, 2)]

if first[1] >= second[0] and second[1] >= first[0]:
    print(max(first[0], second[0]), min(first[1], second[1]))
else:
    print(-1)
