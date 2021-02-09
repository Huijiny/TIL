import sys

sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    lst = list(map(int, input().split(' ')))

    min = lst[0]
    max = lst[0]
    for idx in range(1, len(lst)):
        if min >= lst[idx]:
            min = lst[idx]
        if max <= lst[idx]:
            max = lst[idx]

    print('#{} {}'.format(tc, max-min))


