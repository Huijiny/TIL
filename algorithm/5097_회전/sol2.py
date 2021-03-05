
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    queue = input().split()
    M = M % N
    print(queue[M])