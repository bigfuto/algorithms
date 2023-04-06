import re

N = int(input())
words_dict, lower_dict = set(), set()
pattern = r'[A-Z]'
ans = 0

for _ in range(N):
    word = input()
    words_dict.add(word)
    lower_dict.add(word.lower())

test_text = input().split()

for word in test_text:
    if word.lower() in lower_dict:
        if word in words_dict:
            ans += 1
    elif len(re.findall(pattern, word)) == 1:
        ans += 1

print(len(test_text) - ans)
