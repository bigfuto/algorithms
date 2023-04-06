N, M = map(int, input().split())
Ann = set(int(input()) for _ in range(N))
Boris = set(int(input()) for _ in range(M))

for item in (Ann & Boris, Ann - Boris, Boris - Ann):
    print(len(item))
    print(*sorted(item))
