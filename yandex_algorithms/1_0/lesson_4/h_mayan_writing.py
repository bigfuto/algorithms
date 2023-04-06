g, St = map(int, input().split())
W, S = input(), input()

first_dict, second_dict = {}, {}
ans = 0

for letter in W:
    if letter not in first_dict:
        first_dict[letter] = 0
        second_dict[letter] = 0
    first_dict[letter] += 1

for i in range(g):
    if S[i] in first_dict:
        first_dict[S[i]] -= 1

if first_dict == second_dict:
    ans = 1

for i in range(g, St):
    if S[i] in first_dict:
        first_dict[S[i]] -= 1
    if S[i - g] in first_dict:
        first_dict[S[i - g]] += 1
    if first_dict == second_dict:
        ans += 1

print(ans)
