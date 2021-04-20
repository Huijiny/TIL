import sys
sys.stdin = open('input (5).txt')


def distribute(person, cost):
    global max_p

    if cost <= max_p:
        return

    if person == N:
        max_p = cost
        return

    for i in range(N):
        if not task_done[i]:
            task_done[i] = True
            distribute(person + 1, cost * (P[person][i]/100))
            task_done[i] = False


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    P = [list(map(int, input().split())) for _ in range(N)]
    max_p = 0
    task_done = [False] * N
    distribute(0, 1)
    print("#{} {:.6f}".format(tc, max_p*100))