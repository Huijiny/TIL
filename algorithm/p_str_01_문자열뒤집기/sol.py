"""
1. 내장함수(x)
2. 직접 짜기
3. 재귀로 짜기
"""

word = 'abcdeㅇㄹㄴㅇㄹ'
reversed_word = ''

# 1. 직접짜기

for i in word:
    reversed_word = i + reversed_word
print(reversed_word)  # edcba

# 2. 재귀로 짜기

def swap_string(string):
    if len(string) == 1:
        return string
    else:
        return string[-1] + swap_string(string[0:len(string)-1])
print(swap_string(word))