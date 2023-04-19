def left_search(num, seq1):
    if num < seq1[0]:
        return 0
    left, right = 0, L - 1
    while left < right:
        m = (left + right + 1) // 2
        if seq1[m] <= num:
            left = m
        else:
            right = m - 1
    return left + 1


def right_search(seq1, seq2):
    left = min(seq1[0], seq2[0])
    right = max(seq1[-1], seq2[-1])
    while left < right:
        m = (left + right) // 2
        if left_search(m, seq1) + left_search(m, seq2) >= L:
            right = m
        else:
            left = m + 1
    return left


N, L = map(int, input().split())

seq = []

for i in range(N):
    seq.append(list(map(int, input().split())))

for i in range(N - 1):
    for j in range(i + 1, N):
        print(right_search(seq[i], seq[j]))
