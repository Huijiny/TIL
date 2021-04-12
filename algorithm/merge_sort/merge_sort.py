import sys

sys.stdin = open('input.txt')


def merge_sort(numbers):
    N = len(numbers)
    # base case => numbers 의 길이가 2보다 작다면(0, 1) 그대로 리턴
    if N < 2:
        return numbers

    # 중간점 잡기
    mid_idx = N // 2
    # 중간점 기준 왼쪽 리스트
    left = numbers[:mid_idx]
    # 중간점 기준 오른쪽 리스트
    right = numbers[mid_idx:]

    # 정렬된 왼쪽
    sorted_left = merge_sort(left)
    # 정렬된 오른쪽
    sorted_right = merge_sort(right)

    # 최종 병합된 결과
    merged = []
    l = r = 0
    while l < len(sorted_left) and r < len(sorted_right):
        # 좌/우 맨 앞에서 더 작은 값을 최종 결과에 추가
        if sorted_left[l] < sorted_right[r]:
            merged.append(sorted_left[l])
            l += 1
        else:
            merged.append(sorted_right[r])
            r += 1

    # 좌/우 남은 숫자들은 이미 정렬되어 있으므로, 그대로 병합
    merged += sorted_left[l:]
    merged += sorted_right[r:]

    return merged


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    print(f'#{tc} {merge_sort(arr)}')

