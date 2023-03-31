N, K, M = map(int, input().split())

amount = K // M
rest = K % M
item = (N // K) * amount
metal = N % K + rest * (N // K)

while metal >= K:
    item += (metal // K) * amount
    metal -= (metal // K) * amount + rest * (metal // K)

print(item)
