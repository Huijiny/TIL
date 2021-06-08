def solution(string, n):
    if n == len(string):
        return
    else:
        print(string[n], end="")
        solution(string, n+1)
        print(string[n], end="")
solution('asadadas', 0)