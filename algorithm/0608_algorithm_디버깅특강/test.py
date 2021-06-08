def solution(str):
    dic = dict()
    for s in str:
        dic[s] = dic.get(s, 0) + 1
    max_cnt = 0
    for key, val in dic.items():
        if max_cnt < val:
            max_cnt = val
            max_key = key
    print(max_key, max_cnt)


def sol2(str2):
    for n in range(2, len(str2)):
        dic = dict()
        start = 0
        end = start + n
        real_max_key = 0
        real_max_val = 0
        for str in str2:
            # 구간 n 개씩 자르는 구간.
            str = str2[start:end]

            # 잘린 str 내에서 알파벳 가장 많이 등장하는거 고르기
            for s in str:
                dic[s] = dic.get(s, 0) + 1
            max_cnt = 0
            for key, val in dic.items():
                if max_cnt < val:
                    max_cnt = val
                    max_key = key
            if real_max_val < max_cnt:
                real_max_val = max_cnt
                real_max_key = max_key
            start += n
        print(n, real_max_key)

def sol3(n, str2):
    dic = dict()
    start = 0
    end = start + n
    real_max_key = 0
    real_max_val = 0
    while start != len(str2)-n-1:
        # 구간 n 개씩 자르는 구간.
        str = str2[start:end]
        # 잘린 str 내에서 알파벳 가장 많이 등장하는거 고르기
        for s in str:
            dic[s] = dic.get(s, 0) + 1
        max_cnt = 0
        for key, val in dic.items():
            if max_cnt < val:
                max_cnt = val
                max_key = key
        if real_max_val < max_cnt:
            real_max_val = max_cnt
            real_max_key = max_key
        start += 1
        end = start + n
    print(n, real_max_key)


# solution('aasadabbbbb')
# sol2('ssadadaaasadaaas')
sol3(5, 'ssadadaaasadaaas')