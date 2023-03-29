'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
'''
V, E = map(int, input().split())
arr = list(map(int, input().split()))
adjM = [[0]*(V+1) for _ in range(V+1)]
adjL = [[] for _ in range(V+1)]

for _ in range(E):
    # 2개씩 끊어서 가져오기
    v1, v2 = arr[i*2], arr[i*2+1]
    adjM[v1][v2] = 1
    adjM[v2][v1] = 1

    adjL[v1].append(v2)
    adjL[v2].append(v1)
'''
# 신교수님 풀이
# dfs(1, 7)  s: node 의 인덱스(시작지점 A) / V: 정점 개수

def dfs(s, V):
    # 초기화
    visited = [0] * (V+1)
    stack = []
    # 현재 방문한 정점 : i
    i = s
    visited[i] = 1
    print(node[i])

    while True:
        # 현재 정점 i 에서 탐색할 수 있는 다음 정점 w 에 대해서
        # w 로 가는 길이 있고(1), w를 방문한 적이 없다면(0) w 방문
        for w in range(1, V+1):
            if adj[i][w] == 1 and visited[w] == 0:
                # w 는 길이 있으니까 현 위치 i를 스택에 저장
                stack.append(i)
                # 현 위치 i를 다음 위치 w로 변경
                i = w
                print(node[i])
                # w는 방문했다는 표시
                visited[w] = 1
                # 현 위치 i 에서 더 확인할 필요가 없음
                break # 다른 방향으로 가지 않도록 탐색 종료
            # 내가 i에서 탐색 해봤는데 더이상 탐색할 정점이 없다
            # (break 만난적 없음)
        else:
            # 내가 최근에 방문했던 정점을 스택에 넣어놓았음
            # 하나 꺼내서 그 위치로 돌아간다
            if stack:
                i = stack.pop()
            # 스택이 비어 있다면 종료
            else:
                break
    return

# 인접 행렬
# adjust 이차원 배열
# 연결된 정점 있는지 확인
#       x  A  B  C  D  E  F  G
adj = [[0, 0, 0, 0, 0, 0, 0, 0], # X
       [0, 0, 1, 1, 0, 0, 0, 0], # A
       [0, 1, 0, 0, 1, 1, 0, 0], # B
       [0, 1, 0, 0, 0, 1, 0, 0], # C
       [0, 0, 1, 0, 0, 0, 1, 0], # D
       [0, 0, 1, 1, 0, 0, 1, 0], # E
       [0, 0, 0, 0, 1, 1, 0, 1], # F
       [0, 0, 0, 0, 0, 0, 1, 0]] # G
node = ["", "A", "B", "C", "D", "E", "F", "G"]

'''
정점(V)의 개수, 간선(E)의 개수
7 8
1 2
1 3
2 4
2 5
3 7
4 6
5 6
6 7
'''
# 방법 1. <배열>
'''
V, E = map(int, input().split())
adj = [[0] * (V+1) for _ in range(V+1)] # +1 : 패딩처리
for i in range(E):
    start, to = map(int, input().split())
    adj[start][to] = 1
    # 무향 그래프 (방향이 없는 그래프)만 아래 추가
    adj[to][start] = 1
dfs(1, 7)    # A-B-D-F-E-C-G   ?????


# 방법 2. <인접 리스트>
V, E = map(int, input().split())
adj = [[0] * (V+1) for _ in range(V+1)] # +1 : 패딩처리
# 인접 리스트
# adj_list[i] : i번 정점에 연결되어 있는 정점들의 리스트
adj_list [[] for _ in range(V+1)]
for i in range(E):
    start, to = map(int, input().split())
    adj[start][to] = 1
    # 무향 그래프 (방향이 없는 그래프)만 아래 추가
    adj[to][start] = 1
    # 인접 리스트 사용
    adj_list[start].append(to)
    adj_list[to].append(start)

dfs(1, 7)    # A-B-D-F-E-C-G   G-C?????
'''
# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(r, c, n):
    # 방문체크 배열 2차원으로 만들기
    visited = [[0] * n for _ in range(n)]
    # 스택 초기화
    stack = []
    visited[r][c] = 1

    while True:

        # 현재 위치가 도착지점이라면 탐색 종료
        if arr[r][c] == 3:
            print("도착")
            break

        # 4방향 탐색
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            # 다음 위치 계산 후, 갈 수 있는 곳인지, 이전에 방문하지 않았던 곳인지
            if 0 <= nr < n and 0 <= nc < n and arr[nr][nc] != 1 and not visited[nr][nc]:
                # 돌아올 위치를 스택에 저장 (현재 위치)
                stack.append((r,c)) # 튜플 형식으로 넣기
                visited[nr][nc] = 1
                # 다음 위치로 이동
                r, c = nr, nc
                # 다른 방향으로 탐색 X, 갈 수 있는 방향으로 계속 간다.
                break

            # 4 방향을 모두 살펴봤는데 갈 수 있는 곳이 없다?
        else:
            if stack:
                r, c = stack.pop()
            # 스택에 남아 있는 위치가 없다면 탐색 종료

# 2차원 배열(미로) 0 : 길 / 1 : 벽 / 3 : 도착지점
arr = [[0, 0, 0, 0, 1, 3],
       [1, 1, 1, 0, 1, 0],
       [0, 0, 1, 0, 1, 0],
       [0, 1, 1, 0, 1, 0],
       [0, 1, 1, 0, 1, 0],
       [0, 0, 0, 0, 0, 0]]

dfs(0, 0, 6)


# DFS 재귀버전
'''
def dfs(now):
    print(now)
    # now : 현재 정점 번호
    # 현재 정점에서 방문할수 있는 정점을 찾아서 방문
    for to in range(1, V + 1):
        if adj[now][to] and not visited[to]:
            visited[to] = 1
            dfs(to) # 재귀호출, like stack push

V, E = map(int, input().split())
adj = [[0] * (V + 1) for _ in range(V + 1)]
# 인접 리스트
adj_list = [[] for _ in range(V + 1)]
for i in range(E):
    start, to = map(int, input().split())
    adj[start][to] = 1
    # 무향 그래프 (방향이 없는 그래프)만 아래 추가
    adj[to][start] = 1
    # 인접 리스트 사용
    adj_list[start].append(to)
    adj_list[to].append(start)

visited = [0] * (V + 1)
visited[1] = 1
dfs(1)
'''