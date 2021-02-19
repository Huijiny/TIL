import sys
sys.stdin = open('input (2).txt')

T = int(input())

# for tc in range(1, T+1):
#     N, K = map(int, input().split())
#
#     puzzle = [list(map(int, input().split())) for _ in range(N)]
#
#     ans = 0
#
#     for i in range(N):
#         cnt = 0
#
#         for j in range(N):
#             if puzzle[i][j] == 1:
#                 cnt += 1
#
#             if puzzle[i][j] == 0 or j == N-1:
#                 if cnt == K:
#                     ans += 1
#                 cnt = 0
#
#         for j in range(N):
#             if puzzle[j][i] == 1:
#                 cnt += 1
#             if puzzle[j][i] == 0 or j == N-1:
#                 if cnt == K:
#                     ans += 1
#                 cnt = 0
#     print("#{} {}".format(tc, ans))

for tc in range(1, int(input())+1):
    N, K = map(int, input().split())

    puzzle = [list(map(int, input().split()))+[0] for _ in range(N)]
    puzzle.append([0]*(N+1))

    ans = 0

    for i in range(N):
        cnt = 0
        #벽을 한 칸 더 둘렀기 때문에 증가
        for j in range(N+1):
            if puzzle[i][j]:
                cnt += 1
            else:
                if cnt == K:
                    ans += 1
                cnt = 0
        #열우선순회
        for j in range(N+1):
            if puzzle[j][i]:
                cnt += 1
            else:
                if cnt == K:
                    ans += 1
                cnt = 0