N = int(input())
shoots = set()

for i in range(N):
    x, _ = map(int, input().split())
    shoots.add(x)

print(len(shoots))
