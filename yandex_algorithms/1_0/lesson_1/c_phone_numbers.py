import re

number = [re.sub('\D', '', input()) for _ in range(4)]

if len(number[0]) == 7:
    number[0] = '7495' + number[0]

for i in range(1, 4):
    if len(number[i]) == 11 and number[0][1:11] == number[i][1:11]:
        print('YES')
    elif len(number[i]) == 7 and number[0][1:11] == ('495' + number[i]):
        print('YES')
    else:
        print('NO')
