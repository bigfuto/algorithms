def read_lang(num):
    return set(input() for _ in range(num))


N, M = int(input()),  int(input())
all_lang = read_lang(M)
one_lang = all_lang

for _ in range(N - 1):
    M = int(input())
    temp_lang = read_lang(M)
    all_lang = all_lang | temp_lang
    one_lang = one_lang & temp_lang

print(len(one_lang), *one_lang, len(all_lang), *all_lang, sep='\n')
