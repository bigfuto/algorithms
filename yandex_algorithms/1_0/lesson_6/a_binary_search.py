def binary_search(num):
    left, right = 0, N
    while left < right:
        m = (left + right) // 2
        if first_array[m] > num:
            right = m
        elif first_array[m] < num:
            left = m + 1
        else:
            return 'YES'
    return 'NO'


N, K = map(int, input().split())
first_array = list(map(int, input().split()))
second_array = list(map(int, input().split()))

ans = []

for number in second_array:
    ans.append(binary_search(number))

print(*ans, sep='\n')
