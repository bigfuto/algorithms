text = open('input.txt').read().split()
words = dict.fromkeys(text, 0)
frequent = 0

for word in text:
    words[word] += 1
    frequent = max(frequent, words[word])

print(sorted(key for key, value in words.items() if value == frequent)[0])
