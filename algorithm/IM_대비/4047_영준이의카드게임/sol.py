import sys

sys.stdin = open("sample_input.txt")


def solution(cards):
    if len(set(cards)) != len(cards):
        return "ERROR"
    # S:0, D:1, H:2, C:3
    card_idx = [0] * 4
    for card in cards:
        if card[0:1] == "S":
            card_idx[0] += 1
        elif card[0:1] == "D":
            card_idx[1] += 1
        elif card[0:1] == "H":
            card_idx[2] += 1
        else:
            card_idx[3] += 1
    result = ''
    for i in range(4):
        result += str(13 - card_idx[i]) + ' '
    return result.rstrip()


T = int(input())
for tc in range(1, T + 1):
    result = 0
    string = input()
    cards = [string[i:i + 3] for i in range(0, len(string), 3)]
    print("#{} {}".format(tc, solution(cards)))
