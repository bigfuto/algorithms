n = int(input())
last = float(input())

min_freq = 30.0
max_freq = 4000.0
closer = 'closer'

for i in range(n-1):
    now, cl_or_fr = input().strip().split()
    now = float(now)
    now_freq = (last + now) / 2
    if abs(max_freq - min_freq) < 10 ** (-6):
        continue
    now_max, now_min = max(min_freq, now_freq), min(max_freq, now_freq)
    if cl_or_fr == closer:
        if last < now:
            min_freq = now_max
        else:
            max_freq = now_min
    else:
        if last < now:
            max_freq = now_min
        else:
            min_freq = now_max
    last = now

print(min_freq, max_freq)
