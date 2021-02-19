import sys
sys.stdin = open("input (3).txt")

def manacher(s):
    s = '#' + '#'.join(s) + '#'
    N = len(s)
    cnt_list = [0] * N

    """
    r: 지금까지 확인한 회문들의 가장 먼 우측 인덱스체
    p: 지금까지 확인한 회문들 중 가장 중심 인덱
    """

    r = p = 0
    for idx in range(N):
        if idx <= r:
            m_idx = 2 * p - idx # 중심점. 대척점.
            # 남은 꽃길 길이만큼 갱신
            if cnt_list[m_idx] > r - idx:
                cnt_list[idx] = r - idx
            else: # 대척점 내용으로 갱
                cnt_list[idx] = cnt_list[m_idx]
        """
        세상바깥으로의 모험.
        idx = 나.
        idx - cnt_list[idx] => 현 idx 기준으로 확보한 회문 좌측 끝
        idx + cnt_list[idx] => 현 idx 기준으로 확보한 회문 우측 끝
        idx - cnt_list[idx] - 1 => 미지의 왼쪽
        idx + cnt_list[idx] + 1=> 미지의 오른쪽
        """
        while idx - cnt_list[idx] >= 0 and idx + cnt_list[idx] < N and\
                s[idx - cnt_list[idx] - 1] == s[idx + cnt_list[idx] + 1]:
            cnt_list[idx] += 1

        # 세상끝이 내가 아는 세상 끝보다 크다면. 중심점과 세상 끝 교
        if r < idx + cnt_list[idx]:
            r = idx + cnt_list[idx]
            p = idx

    return max(cnt_list)


length = 100
T = 10
max_ = 1
for tc in range(1, T+1):
    case = int(input())
    matrix = [input() for _ in range(length)]

    for row_list in matrix:
        max_tmp = manacher(row_list)
        if max_ < max_tmp:
            max = max_tmp

    col_matrix = []
    col_list = ''
    for col in range(length):
        for row in matrix:
            col_list += row[col]
        col_matrix.append(col_list)
        col_list = ''

    for col_list in col_matrix:
        max_tmp = manacher(col_list)
        if max_ < max_tmp:
            max = max_tmp


    print("#{} {}".format(tc,))



