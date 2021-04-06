import sys
sys.stdin = open("input (4).txt")
def postorder(n):
    # 자식이 한 명이라도 있어야 재귀 가능 
    if tree[1][n] > 0:
        postorder(tree[1][n])
        postorder(tree[2][n])
        # 현재 노드의 두 자식들의 index값을 저장함
        left = tree[1][n]
        right = tree[2][n]
        # 자식 노드의 값을 연산
        if tree[0][n] == '+':
            tree[0][n] = tree[0][left] + tree[0][right]
        elif tree[0][n] == '-':
            tree[0][n] = tree[0][left] - tree[0][right]
        elif tree[0][n] == '*':
            tree[0][n] = tree[0][left] * tree[0][right]
        else:
            tree[0][n] = tree[0][left] / tree[0][right]


T = 10
for tc in range(1, T+1):
    result = 0
    N = int(input())
    tree = [[0] * (N+1) for _ in range(3)]

    for i in range(1, N+1):
        values = input().split()
        # 현재 노드 인덱스 
        idx = int(values[0])
        # 연산자이면 str그대로, 아니면 Int로 변형해서 저장
        if values[1].isdigit():
            tree[0][idx] = int(values[1])
        else:
            tree[0][idx] = values[1]
        if len(values) > 2:
            tree[1][idx] = int(values[2])
            tree[2][idx] = int(values[3])
            
    postorder(1)

    print("#{} {}".format(tc, int(tree[0][1])))