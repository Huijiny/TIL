import sys
sys.stdin = open('input (4).txt')

def inorder(n):
    if n > 0:
        inorder(left[n])
        print(node[n], end='')
        inorder(right[n])

T = 10
global V
for tc in range(1, T+1):
    V = int(input())
    left = [0] * (V+1)
    right = [0] * (V+1)

    node = [0] * (V+1)
    for i in range(1, V+1):
        values = input().split()
        index = int(values[0])

        node[index] = values[1] # 알파벳 저장
        if len(values) == 3:
            left[index] = int(values[2])
        if len(values) == 4:
            left[index] = int(values[2])
            right[index] = int(values[3])
    print("#{}".format(tc), end=' ')
    inorder(1)
    print()