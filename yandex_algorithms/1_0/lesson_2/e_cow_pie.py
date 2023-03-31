n = int(input())
seq = list(map(int, input().split()))

winners_table = sorted(seq, reverse=True)
winner = winners_table[0]
ans_set = set()
ans = 0

for i in range(seq.index(winner) + 1, n - 1):
    if seq[i] % 10 == 5 and seq[i] > seq[i + 1]:
        ans_set.add(seq[i])

if ans_set:
    while winners_table[ans] not in ans_set:
        ans += 1
    ans += 1

print(ans)
