import sys
sys.stdin = open("sample_input (3).txt")

T = int(input())
for tc in range(1, T+1):
    result = [0]
    n = int(input())
    scores = list(map(int, input().split()))
    checklist = [True]+[False]*10000

    for score in scores:
        tmp = []
        for res in result:
            if not checklist[res+score]:
                checklist[res+score] = True
                tmp.append(score+res)
        result.extend(tmp)
    print("#{} {}".format(tc, len(result)))

    # for score in scores:
    #     tmp = []
    #     for res in result:
    #         if score + res not in result:
    #             tmp.append(score + res)
    #     result.extend(tmp)