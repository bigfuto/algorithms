def left_search(num, seq1):
    if num < seq1[0]:
        return 0
    left, right = 0, L - 1
    while left < right:
        mid = (left + right + 1) // 2
        if seq1[mid] <= num:
            left = mid
        else:
            right = mid - 1
    return left + 1


def right_search(seq1, seq2):
    left = min(seq1[0], seq2[0])
    right = max(seq1[-1], seq2[-1])
    while left < right:
        mid = (left + right) // 2
        if left_search(mid, seq1) + left_search(mid, seq2) >= L:
            right = mid
        else:
            left = mid + 1
    return left


N, L = map(int, input().split())

seq = []

for _ in range(N):
    x1, d1, a, c, m = map(int, input().split())
    temp_seq = [x1]
    for _ in range(1, L):
        x1 = x1 + d1
        temp_seq.append(x1)
        d1 = (d1 * a + c) % m
    seq.append(temp_seq)

for i in range(N - 1):
    for j in range(i + 1, N):
        print(right_search(seq[i], seq[j]))
