N, M, K = map(int, input().split())

field = [[0] * (M + 2) for _ in range(N + 2)]

for _ in range(K):
    p, q = map(int, input().split())
    field[p][q] = 9
    for row in range(-1, 2):
        for column in range(-1, 2):
            field[p + row][q + column] += 1

for i in range(1, len(field) - 1):
    for j in range(1, len(field[0]) - 1):
        print('*', end=' ') if field[i][j] > 8 else print(field[i][j], end=' ')
    print()
