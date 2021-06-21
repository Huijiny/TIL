from collections import defaultdict
from itertools import permutations


def move_and_get_next_xy(board, r, c, dx, dy):
    cur_r, cur_c = r, c
    while True:
        nr = cur_r + dx
        nc = cur_c + dy

        if not (0<=nr<4 and 0<=nc<4):
            return cur_r, cur_c
        if board[nc][nr] != 0:
            return nr, nc
        cur_r = nr
        cur_c = nc


def bfs(start, end, board):
    r, c = start
    nr, nc = end
    q = [(r, c, 0)]

    moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    visited = [[0] * 4 for _ in range(4)]
    while q:
        r, c, cnt = q.pop()
        if visited[r][c]: continue
        visited[r][c] = 1
        if r == nr and c == nc:
            return cnt

        for k, t in moves:
            new_r, new_c = r+k, c+t
            if 0 <= new_r < 4 and 0 <= new_c < 4:
                q.append((new_r, new_c, cnt+1))
            new_r, new_c = move_and_get_next_xy(board, r, c, k, t)
            q.append((new_r, new_c, cnt+1))
    return -1


def solution(board, sr, sc):
    cards = defaultdict(list)


    # 각 점의 좌표들을 저장해놓기
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                cards[board[i][j]].append((i, j))
    # 총 카드의 개수는?
    total_cards_cnt = len(cards)
    # permutation을 통해 총 카드 개수중에 총 카드개수를 뽑아서 순서를 가져오기.
    min_cnt = 1e9

    for order in permutations(cards, total_cards_cnt):
        cnt = 0
        r, c = sr, sc
        # (1, 3, 2)
        for num in order:
            # 1
            cards_dist_list = []
            for nr, nc in cards[num]:
               cards_dist_list.append((bfs((r, c), (nr, nc), board), nr, nc))

            # 첫번째꺼가 더 가까우면 첫번째꺼 먼저 방문해.
            if cards_dist_list[0][0] < cards_dist_list[1][0]:
                cnt += cards_dist_list[0][0]
                cnt += bfs((cards_dist_list[0][1], cards_dist_list[0][2]), (cards_dist_list[1][1], cards_dist_list[1][2]), board)
                r, c = cards_dist_list[1][1], cards_dist_list[1][2]

            else:
                cnt += cards_dist_list[1][0]
                cnt += bfs((cards_dist_list[1][1], cards_dist_list[1][2]), (cards_dist_list[0][1], cards_dist_list[0][2]), board)
                r, c = cards_dist_list[0][1], cards_dist_list[0][2]
        min_cnt = min(min_cnt, cnt)

    return min_cnt + len(cards)*2


print(solution([[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]], 1, 0))
