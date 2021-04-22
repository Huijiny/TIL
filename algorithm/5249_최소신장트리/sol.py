import sys
sys.stdin = open('sample_input (5).txt')

def find(x):
    if p[x] == x:
        return x
    return find(p[x])


def union(x, y):
    x = find(x)
    y = find(y)
    p[y] = x


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    weights = [list(map(int, input().split())) for _ in range(E)]
    p = [i for i in range(V + 1)]
    total = 0
    weights.sort(key=lambda x:x[2])
    # 간선 하나씩 가져와서
    for x, y, w in weights:
        # 양 옆 노드의 부모가 각각 다르다면, 각각 같은 집합에 속하지 않았다면
        if find(x) != find(y):
            union(x, y)
            total += w
    print("#{} {}".format(tc, total))