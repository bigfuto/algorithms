old = int(input())

end = -2000000000
eq, more, less = '0', '0', '0'
options = {
    '000': 'RANDOM',
    '001': 'ASCENDING',
    '010': 'DESCENDING',
    '011': 'RANDOM',
    '100': 'CONSTANT',
    '101': 'WEAKLY ASCENDING',
    '110': 'WEAKLY DESCENDING',
    '111': 'RANDOM',
}

while True:
    new = int(input())
    if new == end:
        break
    if old == new:
        eq = '1'
    elif old > new:
        less = '1'
    else:
        more = '1'
    old = new

print(options[eq + less + more])
