def binary_search(num, end, l, r):
    left, right = 0, end
    while left < right:
        m = (left + right + r) // 2
        if first_array[m] > num:
            right = m - r
        elif first_array[m] < num:
            left = m + l
        else:
            return m
    return left


N, K = map(int, input().split())
first_array = list(map(int, input().split()))
second_array = list(map(int, input().split()))

ans = [0] * K

for i, number in enumerate(second_array):
    first_num = first_array[binary_search(number, N - 1, 1, 0)]
    second_num = first_array[binary_search(number, N - 1, 0, 1)]
    first_diff, second_diff = abs(first_num - number), abs(second_num - number)
    if first_diff < second_diff:
        ans[i] = first_num
    elif first_diff > second_diff:
        ans[i] = second_num
    else:
        ans[i] = min(first_num, second_num)

print(*ans, sep='\n')
