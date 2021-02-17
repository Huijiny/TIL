import sys

sys.stdin = open("GNS_test_input.txt")

T = int(input())

for tc in range(1, T + 1):
    case, n = input().split()
    arr = input().split()
    ex = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    number = [0] * 10
    result = 0

    for i in range(int(n)):
        if arr[i] == 'ZRO':
            number[0] += 1
        elif arr[i] == 'ONE':
            number[1] += 1
        elif arr[i] == 'TWO':
            number[2] += 1
        elif arr[i] == 'THR':
            number[3] += 1
        elif arr[i] == 'FOR':
            number[4] += 1
        elif arr[i] == 'FIV':
            number[5] += 1
        elif arr[i] == 'SIX':
            number[6] += 1
        elif arr[i] == 'SVN':
            number[7] += 1
        elif arr[i] == 'EGT':
            number[8] += 1
        else:
            number[9] += 1

    print(case)
    for i in range(10):
        for _ in range(number[i]):
            print(ex[i], end=' ')
    print()