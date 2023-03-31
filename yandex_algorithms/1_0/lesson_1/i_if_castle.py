A, B, C, D, E = (int(input()) for _ in range(5))

if ((D >= A and (E >= B or E >= C)) or
        (D >= B and (E >= A or E >= C)) or
        (D >= C and (E >= B or E >= A))):
    print('YES')
else:
    print('NO')
