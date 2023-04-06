N = int(input())
word_dict, synonym_dict = {}, {}

for i in range(N):
    word, synonym = input().split()
    word_dict[word], synonym_dict[synonym] = synonym, word

word = input()

if word in word_dict:
    print(word_dict[word])
elif word in synonym_dict:
    print(synonym_dict[word])
