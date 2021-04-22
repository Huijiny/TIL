from collections import deque
import sys
sys.stdin = open('sample_input (5).txt')

def bfs(num):
    count = 0
    # queue생성해서 초기화 하기
    q = deque()
    q.append(num)
    # queue에 값이 있으면.
    while q:
        for _ in range(len(q)):
            # 현재 값을 뽑아서
            cur = q.popleft()
            if num_visited[cur]:
                continue
            num_visited[cur] = True
            # 만약에 계산 결과가
            if cur == M:
                return count
            # 현재 값이 100만 이하이고 아직 정답이 안나왔으면 append
            if 0 < cur + 1 <= 1000000:
                q.append(cur + 1)
            if 0 < cur - 1 <= 1000000:
                q.append(cur - 1)
            if 0 < cur * 2 <= 1000000:
                q.append(cur * 2)
            if 0 < cur - 10 <= 1000000:
                q.append(cur - 10)
        count += 1

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    num_visited = [False] * 1000000
    print("#{} {}".format(tc, bfs(N)))