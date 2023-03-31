N = int(input())
seq = list(map(int, input().split()))

ans = []
tmp = []

if ''.join(map(str, seq)) == ''.join(map(str, seq[::-1])):
    print(0)
else:
    for i in range(len(seq)):
        ans.append(seq[i])
        tmp = seq + ans[::-1]
        if ''.join(map(str, tmp)) == ''.join(map(str, tmp[::-1])):
            print(i + 1)
            print(*ans[::-1])
            break
