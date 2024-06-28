import sys
input = sys.stdin.readline
N = int(input())
word_dict = dict()
for _ in range(N):
    word = input()
    sorted_word = ''.join(sorted(word.strip()))
    if sorted_word not in word_dict:
        word_dict[sorted_word] = 1
    else:
        word_dict[sorted_word] += 1
print(sorted(word_dict.items(), key=lambda x : x[1], reverse=True)[0][1])