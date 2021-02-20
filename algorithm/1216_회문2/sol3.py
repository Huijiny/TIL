import sys
from datetime import datetime
sys.stdin = open('a_test.txt')
def solution(word):
    def is_palindrome(word):
        for idx in range(len(word) // 2):
            if word[idx] != word[-idx - 1]:
                return False
        return True

    def check_max(word, max_val):
        if is_palindrome(word):
            word_length = len(word)
            if max_val < word_length:
                max_val = word_length
        return max_val

    max_val = 1
    for i in range(len(word), max_val, -1):
        if max_val > i:
            break
        else:
            for k in range(len(word) - i + 1):
                word = word[k:k+i]
                max_val = check_max(word, max_val)
                word2 = word[k+1:i]
                max_val = check_max(word2, max_val)
    return max_val

T = int(input())
for tc in range(1, T+1):
    start = datetime.now()
    print(solution(input()))
    end = datetime.now()
    print('#{} {}'.format(10 * 10**tc, end-start))

