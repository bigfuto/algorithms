temp = list(map(int, input().split()))
mode = input()


def check_cond(temp, mode):
	if mode == 'freeze' and temp[0] > temp[1]:
		return temp[1]
	elif mode == 'heat' and temp[0] < temp[1]:
		return temp[1]
	elif mode == 'auto':
		return temp[1]
	return temp[0]


print(check_cond(temp, mode))
