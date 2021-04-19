import sys
sys.stdin = open("sample_input (3).txt")

def quick_sort(numbers, start, end):
    # 종료 조건
    if start < end:
        # 피봇설정 맨 앞에 것.
        pivot = numbers[start]
        left = start + 1
        right = end
        # while 문 종료조건.
        done = False

        while not done:
            # left <= right이고, left가 가리키는 값이 피봇보다 클 때 까지 돌리기.
            while left <= right and numbers[left] <= pivot:
                left += 1
            # left <= right이고, right가 가리키는 값이 피봇보다 작을 때 까지 돌리기.
            while left <= right and numbers[right] >= pivot:
                right -= 1
            # left > right이면 while문 종료조건임
            if left > right:
                done = True
            # 두 점이 가리키는 숫자를 스왑
            else:
                numbers[left], numbers[right] = numbers[right], numbers[left]
        # right가 가리키는 애와 피봇을 스왑.
        numbers[start], numbers[right] = numbers[right], numbers[start]

        # 새로운 피봇 = right를 기준으로 왼쪽과 오른쪽을 나눠 소트
        quick_sort(numbers, start, right - 1)
        quick_sort(numbers, right + 1, end)


for tc in range(1, int(input())+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    quick_sort(numbers, 0, N-1)
    print("#{} {}".format(tc, numbers[N//2]))