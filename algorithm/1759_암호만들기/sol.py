import sys
sys.stdin = open("sample.txt")

L, C = map(int, input().split())
alpha = list(input().split())

alpha.sort()

def check(word):
    mo = 0
    ja = 0
    for al in word:
        if al in ['a', 'e', 'i', 'o', 'u']:
            mo += 1
        else:
            ja += 1
    if mo >= 1 and ja >= 2:
        return True
    return False

def dfs(word, idx):
    if len(word) == L:
        if check(word):
            print(word)
    else:
        for i in range(idx, C):
            dfs(word+alpha[i], i+1)

dfs('', 0)

