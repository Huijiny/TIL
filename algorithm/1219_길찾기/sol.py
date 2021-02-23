import sys
sys.stdin = open("input (3).txt")
def dfs(matrix):
    visited = [0] * 100
    stack = [0]
    visited[0] = 1
    while len(stack) != 0:
        current = stack.pop()
        for i in range(2):
            adj = matrix[i][current]
            if adj == 99:
                return 1
            if visited[adj] != 1:
                stack.append(current)
                visited[adj] = 1
                stack.append(adj)
    return 0

T = 10
for tc in range(1, T+1):
    case, v_num = list(map(int, input().split()))
    matrix = [[-1] * 100 for _ in range(2)]
    V = list(map(int,input().split()))
    for i in range(0, len(V), 2):
        if matrix[0][V[i]] == -1:
            matrix[0][V[i]] = V[i+1]
        else:
            matrix[1][V[i]] = V[i+1]

    print("#{} {}".format(tc, dfs(matrix)))