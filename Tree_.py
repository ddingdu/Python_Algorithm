
'''
4
1 2 1 3 3 4 3 5
'''

# 노드 개수
n = 5
# 간선 개수
e = int(input())
tree = list(map(int, input().split()))

# < 방법1. 인덱스 번호가 부모노드의 번호 > - 왼쪽오른쪽
child_l = [0] * (n+1)
child_r = [0] * (n+1)

# 간선 개수만큼 반복????
for i in range(e):
    parent = tree[i * 2]
    child = tree[i * 2 + 1]
    # 왼쪽 자식이 비어있으면 왼쪽에 추가
    if child_l[parent] == 0:
        child_l[parent] = child
    # 왼쪽 자식이 있으면 오른쪽에 추가
    else:
        child_r[parent] = child

    # 부모 인덱스 : 0  1  2  3  4  5
print(child_l) # [0, 2, 0, 4, 0, 0]
print(child_r) # [0, 3, 0, 5, 0, 0]
print("==========")

# < 방법2. 인덱스 번호가 자식 노드의 번호 > - 조상노드 찾을 때
parent = [0] * (n+1)
for i in range(e):
    p = tree[i * 2]
    c = tree[i * 2 + 1]
    parent[c] = p

  # 자식 인덱스 : 0  1  2  3  4  5
print(parent) # [0, 0, 1, 1, 3, 3]

# Q. 5번 노드의 조상 노드 탐색
now = 5
# parent[now] == 0 이면 now 가 root 노드이기 때문에 부모 노드가 존재하지 않는다.
while parent[now] != 0:
    print(parent[now]) # 3 1
    now = parent[now] # 왜 이거 안넣으면 무한 루프 ????????


'''
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

A=Node("A")
B=Node("B")
C=Node("C")

root=A
A.left=B
A.right=C
'''


# < 연습문제 > 37p
# 트리 정점의 총 수 (V : 13)
'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''
n = int(input())
tree = list(map(int, input().split()))

# 인덱스가 부모노드의 번호
cleft = [0] * (n + 1)
cright = [0] * (n + 1)

# 간선 개수(정점-1)를 범위로 ?????
for i in range(n-1):
    p = tree[i * 2]
    c = tree[i * 2 + 1]
    if cleft[p] == 0:
        cleft[p] = c
    else:
        cright[p] = c
print(cleft)    # [0, 2, 4, 5, 7, 8, 10, 12, 0, 0, 0, 13, 0, 0]
print(cright)   # [0, 3, 0, 6, 0, 9, 11, 0, 0, 0, 0, 0, 0, 0]

# 1. 전위우선 순회 preorder V - L - R / 1 2 4 7 12 3 5 8 9 6 10 11 13
def preorder(t):

    # t 노드가 존재한다면
    if t:
        # 데이터 처리(print)
        print(t, end = ' ')
        # 왼쪽 방문
        preorder(cleft[t])
        # 오른쪽 방문
        preorder(cright[t])

# 2. 중위우선 순회 inorder L - V - R / 12 7 4 2 1 8 5 9 3 10 6 13 11
def inorder(t):
    # t 노드가 존재한다면
    if t:
        # 왼쪽 방문
        inorder(cleft[t])
        # 데이터 처리(print)
        print(t, end = ' ')
        # 오른쪽 방문
        inorder(cright[t])

# 3. 후위우선 순회 postorder L - R - V / 12 7 4 2 1 8 5 9 3 10 6 13 11
def postorder(t):
    # t 노드가 존재한다면
    if t:
        # 왼쪽 방문
        postorder(cleft[t])
        # 오른쪽 방문
        postorder(cright[t])
        # 데이터 처리(print)
        print(t, end = ' ')

preorder(1)
print()
inorder(1)
print()
postorder(1)
print()



# 이진탐색
# 왼쪽 서브트리 루트<현재 노드<오른쪽 서브트리 루트
# 중위순회 LVR
def inorder(t):
    global cnt
    # t 노드가 자연수 n보다 작거나 같다면
    if t <= n:
        # 왼쪽 방문
        inorder(t * 2)
        # 데이터 처리 (인덱스 t에 1씩 증가하면서 넣어주기)
        node[t] = cnt
        cnt += 1
        # 오른쪽 방문
        inorder(t * 2 + 1)

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    node = [0] * (n + 1)

    cnt = 1
    inorder(1)    # 노드 번호 1부터 시작
    # print(node)

    # 루트 노드의 값과 n//2번 노드의 값
    print(f'#{tc} {node[1]} {node[n//2]}')