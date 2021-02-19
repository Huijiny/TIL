import sys
sys.stdin = open("input (3).txt")
T = 10
length = 100
for tc in range(1, T+1):
    result = 0
    case = int(input())
    matrix = []
    for i in range(length):
        matrix.append(input())

    def is_palindrome(word):
        return word == word[::-1]

    def check_max(word, max_tmp):
        if is_palindrome(word):
            word_length = len(word)
            if max_tmp < word_length:
                max_tmp = word_length
        return max_tmp

    max_val = 1

    for row_list in matrix:
        for row in range(length, max_val, -1):
            if max_val > row:
                break
            else:
                for k in range(length-row+1):
                    word = row_list[k:k+row]
                    max_val = check_max(word, max_val)

    col_matrix = []
    col_list = ''
    for col in range(length):
        for row in matrix:
            col_list += row[col]
        col_matrix.append(col_list)
        col_list=''

    for col_list in col_matrix:
        for row in range(length, max_val, -1):
            if max_val > row:
                break
            else:
                for k in range(length-row+1):
                    word = col_list[k:k+row]
                    max_val = check_max(word, max_val)

    print("#{} {}".format(tc, max_val))