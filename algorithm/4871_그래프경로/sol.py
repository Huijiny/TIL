import sys
sys.stdin = open("sample_input (1).txt")
def dfs(V, matrix, S, G):
    stack = [S]
    result = 0
    visited = [0] * V
    visited[S - 1] = 1
    while len(stack) != 0:
        v = stack.pop()

        for row in range(len(matrix[v-1])):
            if matrix[v-1][row] and visited[row] != 1:
                stack.append(v)
                if row + 1 == G:
                    return 1
                stack.append(row + 1)
                visited[row] = 1
                break
    return result
T = int(input())


for tc in range(1, T+1):

    V, E = list(map(int, input().split()))
    matrix = [[0]*V for _ in range(V)]
    for _ in range(E):
        f, t = list(map(int, input().split()))
        matrix[f-1][t-1] = 1
    S, G = list(map(int, input().split()))
    # 여기서 이제 어디갔다가 어디갔다가 어디가는지 찾아야함.
    stack = [S]
    print("#{} {}".format(tc, dfs(V, matrix, S, G)))


"""
# 1. Dictionary
g = {
    'A': ['D', 'C'],
    'B': ['C', 'E'],
    'C': [],
    'D': ['F'],
    'E': [],
    'F': []
}

# 2. ADJ List
g = [
    [], #0
    # 실제 데이
    [4, 5], #1
    [3, 5], #2
    [], #3
    [6], #4
    [], #5
    [], #6
]

# 3. ADJ Matrix

"""