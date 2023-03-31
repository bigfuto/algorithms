sides = [int(input()) for _ in range(3)]

if (sum(sides) - max(sides)) > max(sides):
	print('YES')
else:
	print('NO')
