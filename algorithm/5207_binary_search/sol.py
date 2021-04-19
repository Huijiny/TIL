import sys
sys.stdin = open("sample_input (3).txt")


def binary_search(target, A):
    l = 0
    r = A - 1

    mid = (l + r) // 2

    left_side = right_side = False

    # side 초기화
    if numbers[mid] == target:
        return 1
    elif numbers[mid] < target:
        right_side = True
    else:
        left_side = True

    while l <= r:
        mid = (l + r) // 2
        # if l == r and numbers[mid] != target:
        #     return 0

        if numbers[mid] == target:
            return 1
        elif right_side and numbers[mid] < target: # 타겟이 오른쪽에 포함됨
            l = mid + 1
            left_side = True
            right_side = False
        elif left_side and numbers[mid] > target: # 타겟이 왼쪽에 포함됨
            r = mid - 1
            left_side = False
            right_side = True
        else:
            break
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