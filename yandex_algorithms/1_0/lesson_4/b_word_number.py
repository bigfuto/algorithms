text = open('input.txt').read().split()
numbers = [0] * len(text)
words = {}

for i, word in enumerate(text):
    if word not in words.keys():
        words[word] = -1
    words[word] += 1
    numbers[i] += words[word]

print(*numbers)
