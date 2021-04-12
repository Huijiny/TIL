def traversal(N):
    global result
    # n 이 0 이상일경우 순회하며 개수 체크
    if N > 0:
        result += 1
        traversal(chs[0][N])
        traversal(chs[1][N])


T = int(input())

for tc in range(1, T+1):
    result = 0
    V, N = map(int, input().split())
    # 자식 노드를 담을 배열 정의
    chs = [[0] * (V+1) for _ in range(2)]
    values = list(map(int, input().split()))
    # V-1만큼 돌면서
    for i in range(V-1):
        # 값 두개씩 받아옴
        n1, n2 = values[i*2], values[i*2+1]
        # 부모를 인덱스로 하는 값으
        # 자식 왼쪽 값이 0 이면 넣어주고
        if chs[0][n1] == 0:
            chs[0][n1] = n2
        # 아니면 이미 왼쪽은 차있다는 것이므로 오른쪽에 넣어줌
        else:
            chs[1][n1] = n2
    # 원하는 루트부터 순회 시작
    traversal(N)
    # 자기 자신도 개수에 포함되어있으므로 1 빼줌
    print("#{} {}".format(tc, result-1))