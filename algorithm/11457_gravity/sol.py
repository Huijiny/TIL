import sys
sys.stdin = open("input (2).txt")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))
    count = max_ = 0
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] > numbers[j]:
                count += 1
        if max_ < count:
            max_ = count
        count = 0
    print("#{} {}".format(tc, max_))
