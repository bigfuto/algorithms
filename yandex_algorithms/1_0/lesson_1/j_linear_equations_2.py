a, b, c, d, e, f = (float(input()) for _ in range(6))

det = a * d - b * c
detX = (e * d - b * f)
detY = (a * f - e * c)

if a == b == c == d == e == f == 0:
    print(5)
elif a == b == 0 and e != 0 or c == d == 0 and f != 0:
    print(0)
elif det != 0:
    print(2, detX / det, detY / det)
elif detX == detY == 0:
    if b == d == 0:
        print(3, e / a) if a != 0 else print(3, f / c)
    elif a == c == 0:
        print(4, e / b) if b != 0 else print(4, f / d)
    elif b != 0:
        print(1, -1 * a / b, e / b)
    elif d != 0:
        print(1, -1 * c / d, f / d)
else:
    print(0)
