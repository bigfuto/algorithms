def find_max(mx1, mx2, mx3, num):
    if num >= mx1:
        mx1, mx2, mx3 = num, mx1, mx2
    elif num >= mx2:
        mx2, mx3 = num, mx2
    elif num > mx3:
        mx3 = num
    return mx1, mx2, mx3


def find_min(mn1, mn2, num):
    if num <= mn1:
        mn1, mn2 = num, mn1
    elif num < mn2:
        mn2 = num
    return mn1, mn2


min1 = float('inf')
min2 = min1
max1 = float('-inf')
max2, max3 = max1, max1

for number in map(int, input().split()):
    max1, max2, max3 = find_max(max1, max2, max3, number)
    min1, min2 = find_min(min1, min2, number)

if max1 * max2 * max3 > min1 * min2 * max1:
    print(max1, max2, max3)
else:
    print(max1, min1, min2)
