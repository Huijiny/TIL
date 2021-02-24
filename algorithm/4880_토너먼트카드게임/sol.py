import sys
sys.stdin = open("sample_input (1).txt")
#이닝마러;ㅣㅑㅈ덜;매ㅑㄷ러;매ㅑ덜;매ㅑ더래;쟈덞;쟈덞;쟈더개샞ㄱ끼!!!!!!!!!
def get_winner(first, second):
    if cards[first-1] == '1':
        if cards[second-1] == '1' or cards[second-1] == '3':
            return first
        else:
            return second
    if cards[first-1] == '2':
        if cards[second-1] == '2' or cards[second-1] == '1':
            return first
        else:
            return second
    if cards[first-1] == '3':
        if cards[second-1] == '2' or cards[second-1] == '3':
            return first
        else:
            return second


def divide(start, end):
    if start == end:
        return start
    else:
        first = divide(start, (start+end)//2)
        second = divide((start+end)//2+1, end)
        return get_winner(first, second)
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cards = input().split()
    start = 1
    end = N
    result = divide(start, end)
    print("#{} {}".format(tc, result))