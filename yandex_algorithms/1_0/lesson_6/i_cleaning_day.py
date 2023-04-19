def check_discomfort(discomfort):
    count, j = 0, 0
    while j < discomfort_len:
        if seq[j] <= discomfort:
            count, j = count + 1, j + C - 1
        j += 1
    return count


N, R, C = map(int, input().split())
seq = [int(input()) for _ in range(N)]

seq.sort()
discomfort_len = N - C + 1
left, right = 0, seq[-1] - seq[0]

for i in range(discomfort_len):
    seq[i] = seq[i + C - 1] - seq[i]

while left < right:
    m = (left + right) // 2
    if check_discomfort(m) >= R:
        right = m
    else:
        left = m + 1

print(left)
