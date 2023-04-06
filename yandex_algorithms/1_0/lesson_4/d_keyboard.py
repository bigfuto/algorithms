_ = int(input())
keys = list(map(int, input().split()))
_ = int(input())

for num in map(int, input().split()):
    keys[num - 1] -= 1

for num in keys:
    print('NO') if num >= 0 else print('YES')
