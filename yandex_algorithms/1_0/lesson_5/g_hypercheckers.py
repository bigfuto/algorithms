def find_recur_seq(m):
    temp_numb = seq[m]
    while m < n and seq[m] == temp_numb:
        m += 1
    return m


n, k = map(int, input().split())
seq = list(map(int, input().split()))

seq.sort()
mx = seq[0] * k
temp_num = seq[0]
a, b, e, f, j, ans = 0, 0, 0, 0, 0, 0

for i in range(n):
    if seq[i] == temp_num:
        a += 1
    else:
        while j < n and seq[j] <= mx:
            d = find_recur_seq(j)
            if d - j > 1:
                e += 1
            f, j = f + 1, d
        if a == 1:
            b = 0
        elif a == 2:
            b = 1
        else:
            ans, b = ans + 1, 1
        e, f, a = e - b, f - 1, 1
        ans += (b * f + e) * 3 + ((f * f - f) / 2) * 6
        temp_num = seq[i]
        mx = seq[i] * k
else:
    if a > 2:
        ans += 1

print(int(ans))
