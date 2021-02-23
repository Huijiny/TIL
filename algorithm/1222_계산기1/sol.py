import sys
sys.stdin = open("input (3).txt")

T = 10
for tc in range(1, T+1):
    N = int(input())
    expression = input()
    ex_stack = []
    for idx in range(len(expression)-1, -1, -1):
        ex_stack.append(expression[idx])
    tmp_arr = []
    while len(ex_stack) != 1:
        ex = ex_stack.pop()
        if ex != '+':
            tmp_arr.append(int(ex))
        else:
            tmp_arr.append(int(ex_stack.pop()))
            ex_stack.append(tmp_arr[0]+tmp_arr[1])
            tmp_arr = []

    result = ex_stack.pop()
    print("#{} {}".format(tc, result))