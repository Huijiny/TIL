import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    numbers = list(map(int, input().split()))
    total = 0

    for idx in range(len(numbers)):
        total += numbers[idx]
    avg = total / len(numbers)
    print("#{} {}".format(tc, round(avg)))
