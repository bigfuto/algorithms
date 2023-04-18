n, k = map(int, input().split())
line = input()

sum_in, sum_over, j = 0, 0, 0
ans = [0, 0]
first_dict, second_dict = {}, {}

for i in range(97, 123):
    first_dict[chr(i)] = 0
    second_dict[chr(i)] = 0

for i in range(n):
    while j < n and sum_over == 0:
        if first_dict[line[j]] < k:
            first_dict[line[j]] += 1
            sum_in += 1
        else:
            second_dict[line[j]] += 1
            sum_over += 1
        j += 1
    if sum_in > ans[0]:
        ans[0], ans[1] = sum_in, i + 1
    if second_dict[line[i]] > 0:
        second_dict[line[i]] -= 1
        sum_over -= 1
    else:
        first_dict[line[i]] -= 1
        sum_in -= 1

print(*ans)
