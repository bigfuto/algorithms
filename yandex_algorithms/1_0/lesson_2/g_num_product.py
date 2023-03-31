seq = sorted(list(map(int, input().split())))

if seq[0] * seq[1] > seq[-1] * seq[-2]:
    print(seq[0], seq[1])
else:
    print(seq[-2], seq[-1])
