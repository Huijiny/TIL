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
            current += num
        elif c == 'U':
            current -= num
        elif c == 'Z':
            value = cached.pop()
            table.insert(value, value)
            if value < current:
                current += 1
        else:
            # 지금 삭제되는 값 캐싱
            cached.append(table[current])
            # 테이블에서 삭제하고.
            table.remove(table[current])
            if current == len(table):
                current = len(table) - 1
    i = 0
    j = 0
    while j <= len(table)-1:
        if i == table[j]:
            answer += 'O'
            i += 1
            j += 1
        else:
            answer += 'X'
            i += 1
    return answer