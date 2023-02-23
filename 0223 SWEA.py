import sys
sys.stdin = open('input.txt', 'r')


# 이진 힙
# 최소힙(부모 < 자식) / ans : 마지막 노드의 조상 노드에 저장된 정수의 합
'''
def enq(i):
    global last # 삽입 했다면 마지막 위치 수정해야함
    # 완전이진트리에 마지막 정점에 원소 추가
    last += 1
    heap[last] = i

    c = last      # 현 위치를 자식으로 생각
    p = c // 2    # 부모 위치 찾기
    while p and heap[p] > heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        c = p      # 자리 바꿨으니 자식이 부모가 됨
        p = c // 2 # 아래에서 위로 가니까 // 2
    # return heap

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    heap = [0] * 501
    last = 0    # 마지막에 넣은 원소의 위치
    nums = list(map(int, input().split()))
    ans = 0
    for i in nums:
        enq(i)
    # print(heap)

    # 마지막 노드의 조상 값 더하기
    while last:
        last = last // 2
        ans += heap[last]

    # while n:
    #     n = n // 2
    #     ans += heap[n]
    print(f'#{tc} {ans}')
'''
# 노드의 합
# 후위 순회 L R V (v = left + right)
'''
# < 방법1. 후위순회 함수이용 >
def postorder(t):
    # 트리의 범위 => 노드의 개수
    # 트리의 범위 밖이면
    if t > n:
        return 0

    # 트리의 범위 안이면
    else:
        # 현재 내 값(tree[t])이 0이 아니면 (채워져 있다면 그대로 출력)
        if tree[t] != 0:
            return tree[t]
        # 0 이면 계산 (비어 있다면)
        else:
            # 부모의 번호가 t
            left = postorder(t * 2)
            right = postorder(t * 2 + 1)
            tree[t] = left + right
            return tree[t]

t = int(input())
for tc in range(1, t+1):
    # n: 노드 개수, m: 리프노드 개수, l: 값을 출력할 노드 번호
    n, m, l = map(int, input().split())
    tree = [0] * 1001

    for _ in range(m):
        # leaf: 리프 노드 번호, key: 해당 리프에 저장된 값
        leaf, key = map(int, input().split())
        tree[leaf] = key

    postorder(1)
    print(f'#{tc} {tree[l]}')
# < 방법 2. 함수 없이 반복문으로 >
# t = int(input())
# for tc in range(1, t+1):
#     # n: 노드 개수, m: 리프노드 개수, l: 값을 출력할 노드 번호
#     n, m, l = map(int, input().split())
#     tree = [0] * 1001
# 
#     for _ in range(m):
#         # leaf: 리프 노드 번호, key: 해당 리프에 저장된 값
#         leaf, key = map(int, input().split())
#         # 트리 리프 노드에 값 저장
#         tree[leaf] = key
# 
#     # 값 더해서 노드 아래쪽부터 채워주기
#     for i in range(n, 1, -1): # 인덱스 번호 뒤부터 내림차순으로
#         tree[i // 2] += tree[i]
# 
#     print(f'#{tc} {tree[l]}')
'''

# 세제곱근을 찾아라
'''
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    ans = -1
    for i in range(1000):
        if i ** 3 == n:
            ans = i
    print(f'#{tc} {ans}')
# 100개중 51개 맞음

T = int(input())

for tc in range(1, T + 1):

    n = int(input())

    for i in range(int(n ** (1 / 3) - 1), int(n ** (1 / 3) + 5)):
        if i * i * i == n:
            print(f"#{tc} {i}")
            break
    else:
        print(f"#{tc} -1")
    # for-else : for문이 끝나면 else를 돈다?
'''












