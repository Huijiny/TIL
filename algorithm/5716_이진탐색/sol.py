import sys
sys.stdin = open("sample_input (2).txt")

def inorder(n):
    global count
    if n <= N:
        inorder(n*2)
        tree[n] = count
        count += 1
        inorder(n*2+1)
T = int(input())

for tc in range(1, T+1):
    count = 1
    result = 0
    N = int(input())
    tree = [0] * (N+1)
    tree[1] = int(N/2)+1
    inorder(1)
    print("#{} {} {}".format(tc, tree[1], tree[N//2]))