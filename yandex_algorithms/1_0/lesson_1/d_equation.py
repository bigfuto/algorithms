a, b, c = (int(input()) for _ in range(3))

if c < 0:
    print('NO SOLUTION')
elif a == 0 and b == c ** 2:
    print('MANY SOLUTIONS')
elif a != 0 and (c ** 2 - b) % a == 0:
    print((c ** 2 - b) // a)
else:
    print('NO SOLUTION')
