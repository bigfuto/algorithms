n = int(input())
dots = [[0] * n, [0] * n]
ans = 0

for i in range(n):
    dots[0][i], dots[1][i] = map(int, input().split())

for i in range(n):
    lengths = {}
    wrong_answers = set()
    for j in range(n):
        if i != j:
            len_x = dots[0][i] - dots[0][j]
            len_y = dots[1][i] - dots[1][j]
            length = len_x ** 2 + len_y ** 2
            if (-len_x, -len_y) in wrong_answers:
                ans -= 1
            wrong_answers.add((len_x, len_y))
            if length not in lengths:
                lengths[length] = 0
            lengths[length] += 1
    for value in lengths.values():
        if value > 1:
            ans += ((value - 1) * value) // 2

print(ans)
