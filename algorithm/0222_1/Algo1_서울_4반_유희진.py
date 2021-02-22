import sys
sys.stdin = open("1번_input.txt")

T = int(input())
for tc in range(1, T+1):
    # 정원의 크기인 행 N, 열 M
    N, M = map(int, input().split())
    # 행의 개수만큼 garden에 심어질 나무들을 한줄한줄 가져오기.
    garden = [list(map(int, input().split())) for _ in range(N)]

    # 변수 초기화
    total_cost = expansive_tree = tree_num = expansive_tree_col = 0

    # 왼쪽에서 오른쪽으로 2씩 건너뛰며이동하고,
    for row in range(0, M, 2):
        # 위에서 아래로 이동하면서
        for col in range(N):
            tree_num += 1 # 나무의 개수 추가
            total_cost += garden[col][row] # 나무의 가격 추가
            # 만약 비싼 나무가 현재 가르키는 나무보다 작거나 같다면 비싼 나무와, 열 번호를 각각 갱신
            # 같은 조건을 넣은 이유는, 비싼 나무가 여러개일경우 가장 큰 열의 번호를 계산하므로
            if expansive_tree <= garden[col][row]:
                expansive_tree = garden[col][row]
                expansive_tree_col = row + 1

    print("#{} {} {} {} {}".format(tc, total_cost, tree_num, expansive_tree, expansive_tree_col))