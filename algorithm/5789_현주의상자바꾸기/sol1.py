import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, Q = list(map(int, input().split()))
    boxes = [0] * N
    for i in range(1, Q+1):
        L, R = list(map(int, input().split()))

        for j in range(L-1, R):
            boxes[j] = i
    ans = '#'+str(tc)+' '
    for i in boxes:
        ans += str(i)+' '

    ans.strip()
    print(ans)