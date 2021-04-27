import sys
sys.stdin = open("sample_input (3).txt")

def binary_search(target, A):
    left = 0
    right = A - 1

    mid = (left + right) // 2

    if numbers[mid] == target:
        return 1

    while left <= right:
        mid = (left + right) // 2

        if numbers[mid] == target:
            return 1
        elif numbers[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return 0

T = int(input())
for tc in range(1, T+1):
    A, B = map(int, input().split())
    numbers = sorted(list(map(int, input().split())))
    targets = list(map(int, input().split()))

    result = 0
    for target in targets:
        result += binary_search(target, A)

    print("#{} {}".format(tc, result))