def count_segments(denominator):
    amount = 0
    for i in range(N):
        amount += seq[i] // denominator
    return amount


N, K = map(int, input().split())
seq = [int(input()) for _ in range(N)]

left, right = 0, sum(seq) // K

while left < right:
    m = (left + right + 1) // 2
    if count_segments(m) >= K:
        left = m
    else:
        right = m - 1

print(left)
