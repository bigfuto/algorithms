n = int(input())
ai = list(map(int, input().split()))
m = int(input())

bj = [0] * 1001
ans = 0

for _ in range(m):
    watt, price = map(int, (input().split()))
    if bj[watt] == 0 or bj[watt] > price:
        bj[watt] = price

max_price = max(bj)

for i in range(1000, 0, -1):
    if bj[i] == 0 or bj[i] > max_price:
        bj[i] = max_price
    elif bj[i] < max_price:
        max_price = bj[i]

for i in range(n):
    ans += bj[ai[i]]

print(ans)
