def solution(n, k, cmd):
    answer = ''
    table = list(range(n))
    current = k
    cached = []
    for c in cmd:
        if len(c) > 1:
            c, num = c.split(' ')
            num = int(num)
        if c == 'D':
            while num > 0 and current < n:
                current += 1
                if table[current] != -1:
                    num -= 1

        elif c == 'U':
            while num > 0:
                current -= 1
                if table[current] != -1:
                    num -= 1
        elif c == 'Z':
            value = cached.pop()
            table[value] = value
        else:
            # 지금 삭제되는 인덱 캐싱
            cached.append(current)
            # 테이블에서 삭제하고.
            table[current] = -1
            tmp_cur = current
            while current < n:
                if table[current] != -1:
                    break
                current += 1

            if current == n:
                current = tmp_cur
                while current >= 0:
                    if table[current] != -1:
                        break
                    current -= 1

    for i in table:
        if i == -1:
            answer += 'X'
        else:
            answer += 'O'
    return answer

solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"])