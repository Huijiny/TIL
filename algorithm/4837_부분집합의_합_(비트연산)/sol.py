# import sys
#
# sys.stdin = open("sample_input.txt")
#
# T = int(input())
#
#
# def check(arr, N, K):
#     total = 0
#     for i in range(len(arr)):
#         total += arr[i]
#     if total == K and len(arr) == N:
#         return True
#     else:
#         return False
#
#
# for tc in range(1, T + 1):
#     count = 0
#     result = 0
#     N, K = map(int, input().split())  # N개의 원소를 갖고 원소의 합이 K인 부분집합의 개수
#
#     n = 12
#     arr = list(range(1, n + 1))
#     for i in range(1 << n):  # 원소의 개수 12개
#         tmp_arr = []
#         for j in range(n + 1):  # 원소의 수만큼 비트를 비교함
#             if i & (1 << j):  # i의 j번째 비트가 1이면 j번째 원소 출력
#                 count += 1
#                 tmp_arr.append(arr[j])
#         if check(tmp_arr, N, K):
#             result += 1
#
#     print("#{} {}".format(tc, result))
#
#
#
import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())

    # 일단 N까지의 자연수를 원소로 갖는 리스트 생
    main_list = list(range(1, N+1))
    # 부분집합 전부 만들어서 리스트에 저장
    big_list = []
    for i in range(1<<N):
        sub_list = []
        for j in range(N+1):
            if i & (1<<j):
                sub_list.append(main_list[j])
        big_list.append(sub_list)
    print(big_list)

    # 부분집합 중에서 원소의 갯수가 N개 인것만 추려서 리스트에 저장
    len_list = []
    for i in big_list:
        if len(i) == N:
            len_list.append(i)
    print(len_list)

    # 합이 K이면 갯수 카운트
    result = 0
    for i in len_list:
        if sum(i) == K:
            result += 1

    print('#{} {}'.format(tc, result))
    print(1<<3)
    print(1<<2)
    print(1<<1)
    print(1<<0)