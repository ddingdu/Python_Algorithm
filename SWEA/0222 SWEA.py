import sys
sys.stdin = open('../23.03.29_분할정복/input.txt', 'r')

# subtree
# 노드 n을 루트로 하는 서브 트리에 속한 노드의 개수
'''
# 중위 순회
def preorder(t):
    global cnt
    if t:
        cnt += 1
        preorder(cleft[t])
        preorder(cright[t])

    return cnt

t = int(input())
for tc in range(1, t+1):
    # e : 간선의 개수, n : 루트 노드
    e, n = map(int, input().split())
    tree = list(map(int, input().split()))
    cnt = 0

    # 인덱스 번호가 부모노드의 번호
    cleft = [0] * (e + 2)
    cright = [0] * (e + 2)

    # 간선 개수 만큼 반벅
    for i in range(e):
        p = tree[i * 2]
        c = tree[i * 2 + 1]
        # 왼쪽 자식 비어있다면
        if cleft[p] == 0:
            cleft[p] = c
        else:
            cright[p] = c
    print(cleft)
    print(cright)

    print(f'#{tc} {preorder(n)}')
'''

# 이진탐색
'''
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
'''









