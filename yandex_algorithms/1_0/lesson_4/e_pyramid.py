N = int(input())
blocks = {}

for _ in range(N):
    width, height = map(int, input().split())
    if width not in blocks:
        blocks[width] = height
    blocks[width] = max(height, blocks[width])

print(sum(blocks.values()))
