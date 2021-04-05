def findLeafNode(parent_key, data, word):
    big_result = []
    result = []
    find_parent = False
    for d in data:
        info = d.split(' ')
        if info[2] == parent_key:
            find_parent = True
            pre_level = findLeafNode(info[0], data, word)
            # 전단계에서 받은 값이 -1이면 현재가 리프노드이므로 리프노드인거 추가하고 리턴.끝
            print(pre_level)
            if pre_level == -1:
                if word in info[1]:
                    result.append([info[1]])
                return result

            else:
                for pre in pre_level:
                    pre.append(info[1])
                result = pre_level

    if not find_parent:
        return -1  # 끝남표

    return result


def solution(data, word):
    ROOT = '0'
    answer = findLeafNode(ROOT, data, word)

    return answer


print(solution(["1 BROWN 0", "2 CONY 0", "3 DOLL 1", "4 DOLL 2", "5 LARGE-BROWN 3", "6 SMALL-BROWN 3", "7 BLACK-CONY 4",
                "8 BROWN-CONY 4"], "BROWN"))
