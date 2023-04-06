import re


key_words, dict_match = [], {}
maximum, ans = 0, ''
pattern = {'no': r'\b[a-zA-Z_][a-zA-Z0-9_]*',
           'yes': r'\b(?:[0-9]+[a-zA-Z_]+[a-zA-Z0-9_]*)|(?:[a-zA-Z_][a-zA-Z0-9_]*)'}

file = open('input.txt')
param = next(file).split()

for _ in range(int(param[0])):
    line = next(file)[:-1]
    if param[1] == 'no':
        line = line.lower()
    key_words.append(line)

text = file.read()
file.close()

if param[1] == 'no':
    text = text.lower()

match = re.findall(pattern[param[2]], text, flags=re.ASCII)

for word in match:
    if word not in key_words:
        if word not in dict_match:
            dict_match[word] = 0
        dict_match[word] += 1

for key, value in dict_match.items():
    if value > maximum:
        maximum, ans = value, key

print(ans)
