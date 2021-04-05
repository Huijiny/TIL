def preorder(n):
    if n>0:
        print(n, end='')
        preorder(left[n])
        preorder(right[n])

V, E = map(int, input().split())
edge = list(map(int, input().split()))

left = [0]*(V+1)
right = [0]*(V+1)

pa = [0]*(V+1)

for i in range(E):
    n1, n2 = edge[i*2], edge[i*2+1] #n1 부모, n2 자식노드
    if left[n1] == 0:# 왼쪽 자식이 없으면
        left[n1] = n2 # 부모
    else:
        right[n1] = n2 # 부모를 인덱스로 자식번호 저장
    pa[n2] = n1 # 자식을 인덱스로 부모를 저장

root = 0
for i in range(1, V+1):
    if pa[i] == 0:
        root = i
        break
    print(root)
