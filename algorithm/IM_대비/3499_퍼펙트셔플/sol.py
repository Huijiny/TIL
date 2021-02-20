import sys
sys.stdin = open("sample_input.txt")

def solution(N, cards):
    shuffled = ''
    length = len(cards)
    if N % 2:
        first = cards[0:length//2+1]
        second = cards[length//2+1: length]
        for i in range(length//2):
            shuffled += first[i] + ' ' + second[i] + ' '
        shuffled += first[len(first)-1]
    else:
        first = cards[0:length//2]
        second = cards[length//2: length]
        for i in range(length//2):
            shuffled += first[i] + ' ' + second[i] + ' '
    return shuffled.rstrip()

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cards = input().split()

    print("#{} {}".format(tc, solution(N, cards)))