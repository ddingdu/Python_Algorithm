# < 라이브 교수님 최대 힙 구현 >

def enq(n):
    global last
    # 마지막 정점 추가
    last += 1    # 완전이진트리에 마지막 정점을 추가
    heap[last] = n    # 마지막 정점에 저장
    # 부모가 있고, 부모 > 자식 조건 검사를 위해
    c = last
    p = c // 2
    while p > 0 and heap[p] < heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        # 옮긴 자리에서 부모와 비교하기 위해 (그 부모를 새로운 자식으로 두고 또 비교)
        c = p
        p = c // 2
    return

def deq():
    global last
    tmp = heap[1]   # 루트 임시저장
    heap[1] = heap[last]    # 마지막 정점의 값을 루트로 이동
    # 마지막 정점 삭제
    last -= 1   # 나중에 덮어 씌울 것이므로 0 같은거 저장 안함
    # 자식 중에 큰 애를 찾아서 비교
    p = 1   # 일단 루트를 부모로 두기
    c = p * 2   # 왼쪽 자식 번호 계산
    # 자식이 있는지 확인해야함. 없으면 그냥 끝!
    while c <= last:    # 자식이 하나 이상 있다면 반복 ( last : 의 정점 개수)
        # 오른쪽 자식도 있고, 오른쪽 자식 키가 더 크다면
        if c + 1 <= last and heap[c] < heap[c + 1]:
            c += 1  # 비교 대상을 오른쪽 자식으로 변경
        # 자식이 부모보다 크다면 키 값 교환해~
        if heap[c] > heap[p]:
            heap[c], heap[p] = heap[p], heap[c]
            p = c
            c = p * 2
        else:
            break
    # 루트 꺼내둔거 돌려놓기
    return tmp


heap = [0] * 101    # 완전이진트리 1~100번 인덱스 준비
last = 0    # 완전이진트리의 마지막 정점 번호

enq(5)
print(heap[1])
enq(15)
print(heap[1])
enq(8)
print(heap[1])
enq(20)
print(heap[1])

print(last)    # 4 : 정점의 개수
print(heap)    # [0, 20, 15, 8, 5, 0, ... ]

# 정점이 남아있으면
while last > 0:
    print(deq())
print(heap)    # [0, 5, 5, 8, 5, 0, ... ]



# < 신교수님 최대 힙 구현 >

import random

heap = [0] * 101
last = 0

def enq(item):
    # 삽입 했다면 마지막 위치를 수정 해야함
    global last
    last += 1    # 마지막 위치에 원소 추가
    heap[last] = item

    # 부모가 있고, 부모 > 자식 조건 검사를 위해
    c = last
    p = c // 2
    # 부모 노드가 존재하고, 자식이 부모보다 작을 때까지
    while p and heap[p] < heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        # 자리 바꿨으면 자식의 위치를 다시 바꾸고 계속 진행
        c = p
        p = c // 2 # 아래에서 위로 가니까 //2 ?????

def deq():
    # 마지막 원소 위치를 바꿔줘야 함으로
    global last
    # 루트 노드를 삭제하기 전에 기억
    tmp = heap[1]
    # 마지막 노드를 삭제해서 루트 위치에 땡겨온다.
    heap[1] = heap[last]
    last -= 1 # 마지막 노드 위치 1 감소
    # 루트부터 자리 찾기 (비교해서 나보다 큰값이 자식 중에 있으면 자리 교환)
    p = 1
    c = p * 2 # 왼쪽 자식을 기준으로 (완전이진트리이므로 왼쪽 없으면 오른쪽도 없음)
    while c <= last:    # 자식 위치가 트리 범위 내 존재 할 동안
        # 만약 오른쪽 자식(heap[c+1])이 있다면, 둘 중에 큰 자식과 비교를 한다.
        if c + 1 <= last and heap[c] < heap[c + 1]:
            c = c + 1 # 비교 대상을 오른쪽 자식으로
        if heap[p] < heap[c]:
            # 자식이 더 크면 자리를 교환
            heap[p], heap[c] = heap[c], heap[p]
            p = c
            c = p * 2 # 위에서 아래로 가니까 *2 ?????
        else:
            # 밑에는 어차피 나보다 작은 애들만 있으니까 더 이상 갈 필요 없음
            break
    # 루트 값 반환
    return tmp


for i in range(10):
    enq(random.randrange(1, 10001))
print(heap)

for i in range(10):
    print(deq(), end=' ')


# 파이썬 힙 라이브러리 기본 : 최소 힙
'''
import heapq

hq = []

for i in range(10):
    heapq.heappush(hq, i)
for i in range(10):
    print(heapq.heappop(hq), end=' ')
print()    # 0 1 2 3 4 5 6 7 8 9

# 응용
heapq.heappush(hq, (4, "4등"))
heapq.heappush(hq, (2, "2등"))
heapq.heappush(hq, (1, "1등"))
heapq.heappush(hq, (3, "3등"))

for i in range(4):
    print(heapq.heappop(hq), end=' ')
print()    # (1, '1등') (2, '2등') (3, '3등') (4, '4등')


# 최대 힙
for i in range(10):
    heapq.heappush(hq, (-i, i))    # 우선순위를 뒤집어서 넣으면 최대 힙처럼 쓸 수 있음
for i in range(10):
    print(heapq.heappop(hq), end=' ')
print()    # (-9, 9) (-8, 8) (-7, 7) (-6, 6) (-5, 5) (-4, 4) (-3, 3) (-2, 2) (-1, 1) (0, 0)
'''
