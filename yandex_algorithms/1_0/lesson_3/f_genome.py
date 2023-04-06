first, second = input(),  input()
pairs = set(second[i:i + 2] for i in range(len(second) - 1))
ans = 0

for i in range(len(first) - 1):
    if first[i:i + 2] in pairs:
        ans += 1

print(ans)
