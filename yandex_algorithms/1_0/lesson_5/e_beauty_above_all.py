N, K = map(int, input().split())
seq = tuple(map(int, input().split()))

grades = {}
amount, now_amount = 260000, 0
left, right, j = 0, 0, 0

for i in range(N - K + 1):
    if len(grades) < K:
        while j < N and len(grades) < K:
            j += 1
            if seq[j - 1] not in grades:
                grades[seq[j - 1]] = 0
            now_amount += 1
            grades[seq[j - 1]] += 1
    if grades[seq[i]] > 1:
        now_amount -= 1
        grades[seq[i]] -= 1
    elif len(grades) == K:
        if amount > now_amount:
            amount, left, right = now_amount, i + 1, j
            if amount == K:
                break
        del grades[seq[i]]
        now_amount -= 1

print(left, right)
