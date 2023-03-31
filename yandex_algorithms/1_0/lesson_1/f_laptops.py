sides = list(map(int, input().split()))

side1_temp, side2_temp = 0, 0
side1, side2 = 2000, 2000
k = 2

for i in range(2):
    k -= 1
    m = 4
    for j in range(2, 4):
        m -= 1
        side1_temp = sides[k] + sides[m]
        if sides[i] > sides[j]:
            side2_temp = sides[i]
        else:
            side2_temp = sides[j]
        if side1 * side2 > side1_temp * side2_temp:
            side1, side2 = side1_temp, side2_temp

print(side1, side2)
