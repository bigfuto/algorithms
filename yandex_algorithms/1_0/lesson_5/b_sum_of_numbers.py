N, K = map(int, input().split())
numbers = list(map(int, input().split()))

j, ans = 0, 0
prefix_sum = [0] * (N + 1)

for i in range(N):
    prefix_sum[i + 1] = prefix_sum[i] + numbers[i]
    if prefix_sum[i + 1] - prefix_sum[j] == K:
        ans += 1
    while j <= i + 1 and prefix_sum[i + 1] - prefix_sum[j] > K:
        j += 1
        if prefix_sum[i + 1] - prefix_sum[j] == K:
            ans += 1

print(ans)
