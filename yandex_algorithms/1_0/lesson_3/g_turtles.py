N = int(input())
turtles = set(input() for _ in range(N))
ans = 0

for turtle in turtles:
    a, b = map(int, turtle.split())
    if abs(a) + abs(b) == N - 1:
        ans += 1

print(ans)
