import sys
sys.stdin = open("sample_input (5).txt")

# x의 부모가 나 자신이 아니면 부모를 찾으러 다시 올라감.
# 나 : 부모 이렇게 적혀있으므로
# 부모 : 부모의 부모 이렇게 적혀있으면 부모의 부모를 찾으러 가는거고,
# 부모 : 부모자신 이렇게면 그 부모가 루트라는 뜻.
def find(x):
    # 루트 노드는 부모 노드 번호로 자기 자신을 가진다.
    if parent[x] == x:
        return parent[x]
    # 각 노드의 부모 노드를 찾아 올라간다.
    return find(parent[x])

# 두 집합을 합치기 위해서 배열의 모든 원소를 순회하면서 하나의 집합 번호를 나머지 한 개의 집합번호로 교체
def union_find(x, y):
    # u와 v가 속한 트리의 루트 노드를 찾는다.
    x = find(x)
    y = find(y)

    parent[x] = y

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    values = list(map(int, input().split()))
    # make-set 부분. 자기 자신은 자기 자신의 집합에 포함되어 있다.
    parent = [i for i in range(N+1)]
    # 두 집합을 합치기 위해서 배열의 모든 원소를 순회하면서 하나의 집합 번호를 나머지 한 개의 집합번호로 교체
    # 첫번째 값과 두번째 값을 각각 union 한다.

    for i in range(M):
        union_find(values[i*2], values[i*2+1])
    result = set()
    # 각 원소의 부모를 찾아서 더해주고 set으로 묶어주면 중복제거가 됌.
    for p in parent:
        result.add(find(p))
    # 맨 앞에 0 빼주기.
    print("#{} {}".format(tc,len(result)-1))