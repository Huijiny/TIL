import sys
sys.stdin = open("sample_input.txt")

T = int(input())

for tc in range(1, T+1):
    max_len = 0
    letters = []
    for _ in range(5):
        letter_list = list(input())
        letters.append(letter_list)
        if max_len < len(letter_list):
            max_len = len(letter_list)

    sentence = ''
    for row in range(max_len):
        for col in range(5):
            if row > len(letters[col])-1:
                continue
            sentence += letters[col][row]

    print("#{} {}".format(tc, sentence))