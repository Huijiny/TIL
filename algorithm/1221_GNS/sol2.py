import sys
sys.stdin = open("GNS_test_input.txt")

T = int(input())
for tc in range(1, T + 1):
    case, n = input().split()
    arr = input().split()
    ex = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    number = [0] * 10

    for a_num in arr:
        for idx in range(10):
            if ex[idx] == a_num:
                number[idx] += 1

    print(case)
    for i in range(10):
        for _ in range(number[i]):
            print(ex[i], end=' ')
    print()