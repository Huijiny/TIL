import sys
sys.stdin = open("sample_input.txt")

T = int(input())
for tc in range(1, T + 1):
    N, M = list(map(int, input().split()))
    matrix = []
    for i in range(N):
        matrix.append(list(input()))
    result = ''

    def is_palindrome(word):
        for i in range(len(word) // 2):
            if word[i] != word[-1 - i]:
                return False
        return True

    for col in range(N):
        for row in range(N):
            if row+M <= N:
                word = ''
                for idx in range(row, row+M):
                    word += matrix[col][idx]
                if is_palindrome(word):
                    result = word
                    break

    for row in range(N):
        for col in range(N):
            if col+M <= N:
                word = ''
                for idx in range(col, col+M):
                    word += matrix[idx][row]
                if is_palindrome(word):
                    result = word
                    break

    print("#{} {}".format(tc, result))