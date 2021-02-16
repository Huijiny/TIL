import sys
sys.stdin = open("sample_input.txt")


def binary_search(page, target):
    left = 1
    right = page
    count = 0
    while left <= right:
        mid = int((left + right) / 2)
        if mid == target:
            return count
        elif mid < target:
            left = mid
            count += 1
        elif mid > target:
            right = mid
            count += 1


T = int(input())
for tc in range(1, T + 1):
    page, A, B = map(int, input().split())

    countA = binary_search(page, A)
    countB = binary_search(page, B)
    if countA > countB:
        result = 'B'
    elif countA < countB:
        result = 'A'
    else:
        result = 0
    print("#{} {}".format(tc, result))
