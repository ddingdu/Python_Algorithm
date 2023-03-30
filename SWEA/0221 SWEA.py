import sys
sys.stdin = open('../input.txt', 'r')

# 암호 생성기 (원형 큐, 교수님 풀이)
'''
for tc in range(1, 11):
    _ = int(input())
    password = list(map(int, input().split()))
    n = 8
    q = [0] * (n + 1)
    front = rear = 0

    for i in range(n):
        rear = (rear + 1) % n
        q[rear] = password[i]

    number = 1
    while True:
        # 비밀번호 하나 꺼내서 number를 빼준 후에 다시 큐에 추가
        front = (front + 1) % n
        item = q[front]
        item -= number

        # 숫자 꺼냈는데 0 이하 = 비밀번호 완성
        # 0 으로 바꾸고, 큐 맨 뒤에 삽입
        if item <= 0:
            item = 0
            rear = (rear + 1) % n
            q[rear] = item
            break
        else:
            # 0 보다 크다면 그냥 큐의 맨 뒤에 넣기
            rear = (rear + 1) % n
            q[rear] = item
            # 다음 뺄 수를 1씩 증가
            number += 1
            if number > 5:
                number = 1
    print(f'#{tc}', end=' ')

    for i in range(8):
        front = (front + 1) % n

        print(q[front], end=' ')
    print()
'''

# < 노드의 거리 >
'''
# 출발 노드에서 최소 몇 개의 간선을 지나면 도착 노드에 갈 수 있는지?
# G: 그래프 정보, v: 시작 정점, e : 끝 정점, N: 정점 크기
def bfs(G, v, N):
    visited = [0] * (N+1)
    q = [v]
    visited[v] = 1

    while q:
        t = q.pop(0)
        # print(t, end=' ')
        for i in G[t]:
            if not visited[i]:
                q.append(i)
                visited[i] = visited[t] + 1

    return visited

t = int(input())
for tc in range(1, t+1):
    # V: 정점 개수, E: 노드 개수
    V, E = map(int, input().split())

    G = [[] for _ in range(V + 1)]

    for _ in range(E):
        n1, n2 = map(int, input().split())
        G[n1].append(n2)
        G[n2].append(n1)

    # sn: 출발 노드, gn: 도착 노드
    sn, gn = map(int, input().split())

    visit = bfs(G, sn, V)
    # print(G)

    # < 방법 1 >
    # if visit[gn]:
    #     ans = visit[gn] - visit[sn]
    # else:
    #     ans = 0
    # < 방법 2 >
    ans = visit[gn] - 1 if visit[gn] else 0
    print(f'#{tc} {ans}')


# 교수님 풀이

# G: 그래프 정보, s: 시작, e: 도착, V: 노드 개수
def bfs(G, s, e, V ):
    visited = [0] * (V + 1)
    q = [s]
    q.append(s)
    visited[s] = 1

    while q:
        # 위치 하나 q 에서 꺼내기
        t = q.pop(0)

        for nt in G[t]:
            if not visited[nt]:
                # 방문 처리 & 거리 계산
                q.append(nt)
                visited[nt] = visited[t] + 1
                # 다음 위치 nt가 목표 위치 e와 같다면
                if nt == e:
                    return visited[nt] - 1
    # 중간에 목표 지점을 만나지 못했다 ==> 길이 없음
    return 0

t = int(input())
for tc in range(1, t+1):
    # V: 노드 개수, E: 간선 개수
    V, E = map(int, input().split())
    G = [[] for _ in range(V + 1)]

    for _ in range(E):
        n1, n2 = map(int, input().split())
        G[n1].append(n2)
        G[n2].append(n1)
    # sn: 출발 노드, gn: 도착 노드
    s, e = map(int, input().split())

    print(f'#{tc} {bfs(G, s, e, V)}')
'''

# < BFS 미로의 거리 >
# 최소 몇 칸을 지나야 도착지점에 닿을 수 있는지, 경로 없으면 0
'''
def is_valid(r, c):
    return 0 <= r < n and 0 <= c < n

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]
    r, c = 0, 0

    # 시작위치 (2) 찾기
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:
                r, c = i, j
    # 방문 배열 만들기
    visited = [[0] * n for _ in range(n)]
    # 큐 생성 & 인큐 & 방문 기록
    q = []
    q.append((r, c))
    visited[r][c] = 1

    # 거리 계산 (0에서 시작하기 위해 초깃값을 -1 로 ??)
    distance = -1
    # 중간에 답 찾았는지
    find = False

    # 큐에 값이 있는 동안
    while q:
        # 큐의 길이(원소의 개수)로 반복 횟수 제한
        size = len(q)
        distance += 1

        for _ in range(size):
            # 위치 하나 꺼내기
            r, c = q.pop(0)

            for d in range(4):
                nr, nc = r + dr[d], c + dc[d]
                if is_valid(nr, nc) and arr[nr][nc] != 1 and not visited[nr][nc]:
                    # 다음 위치 인큐 & 방문 기록
                    q.append((nr, nc))
                    visited[nr][nc] = 1

                    # 다음 위치가 목표 위치 (3) 이라면
                    if arr[nr][nc] == 3:
                        q = []    # while 문 중단시키기 위해 초기화
                        find = True
                        break   # 4방향 탐색만 중단
            if find:
                break    # 빈 큐일 경우 pop 했을 때 오류 방지
    # 중간에 도착지점을 만나지 못한 경우, 답 0
    if not find:
        distance = 0

    print(f"#{tc} {distance}")
'''

# <미로 1> - 과제

# 16 * 16 행렬 / 길(0), 벽(1) / 출발(2), 도착(3)
# 도착 가능하면 = 1, 불가능하면 = 0
def is_valid(r, c):
    return 0 <= r < n and 0 <= c < n

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for tc in range(1, 11):
    _ = int(input())
    n = 16
    arr = [list(map(int, input())) for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    distance = 0
    r, c = 1, 1
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:
                r, c = i, j
    # 큐 생성 & 인큐 & 방문 기록
    q = []
    q.append((r, c))
    visited[r][c] = 1

    distance = -1

    find = False

    while q:
        size = len(q)
        distance += 1

        for _ in range(size):
            r, c = q.pop(0)

            for d in range(4):
                nr, nc = r + dr[d], c + dc[d]
                if is_valid(nr, nc) and arr[nr][nc] != 1 and not visited[nr][nc]:
                    # 다음 위치 인큐 & 방문 기록
                    q.append((nr, nc))
                    visited[nr][nc] = 1

                    # 다음 위치가 목표 위치 (3) 이라면
                    if arr[nr][nc] == 3:
                        q = []  # while 문 중단시키기 위해 초기화
                        find = True
                        break  # 4방향 탐색만 중단
            if find:
                break
    if not find:
        distance = 0

    ans = 1 if distance > 0 else 0
    print(f"#{tc} {ans}")
















