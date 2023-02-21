# BFS 알고리즘
'''
def BFS(G, v): # G: 그래프, v: 탐색 시작점, n: 정점 개수
    # visited 생성 / 큐 생성 / 시작점 enqueue
    visited = [0] * (n + 1) # 1번 부텨 n 번까지
    queue = []
    queue.append(v) # enqueue (시작점 v를 큐에 삽입)
    visited[v] = 1  # 시작점 방문 표시 ('enqueue 되었음을 표시')
    while queue:    # 큐가 비어있지 않은 경우
        t = queue.pop(0)    # t : 큐 첫번째 원소 반환
        if not visited[t]:
            visited[t] = True   # 방문 표시
            visit(t)    # 정점 t에서 할일 ???
            for i in G[t]:  # t 와 연결된 모든 정점에 대해
                # 방문되지 않은 곳이라면 큐에 넣기
                if not visited[i]:
                    queue.append(i)
'''

# < 연습문제 3 >
'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
# v : 시작점
def bfs(v, N):
    # visited 생성
    visited = [0] * (N + 1)
    # 큐 생성하고, 시작점 인큐
    q = [v] # ?????????????????
    # 시작점 인큐 표시 (visited 기록)
    visited[v] = 1

    # 큐가 비어있지 않으면
    while q:
        # 디큐
        t = q.pop(0)
        print(t, end = ' ') # t에서 처리할 일 ??????? (방문 순서 출력)
        # t에 인접이고, 방문한적 없는 v
        for i in adjL[t]:
            if visited[i] == 0:
                # v 인큐
                q.append(i)
                # v 인큐되었음 표시
                visited[i] = visited[t] + 1
                # ????
                # visited[v] = visited[t] + 1 이 아까 visited[i] = visited[n] + 1이군여
    print()
    print(visited)  # [0, 1, 2, 2, 3, 3, 4, 3]
# V : 정점 개수  / E : 노드 개수
V, E = map(int, input().split())
arr = list(map(int, input().split()))
# 인접 리스트 ???
adjL = [[] for _ in range(V + 1)] # 1번 부터 V 번까지
for i in range(E):
    n1, n2 = arr[i * 2], arr[i * 2 + 1]
    # 방향 표시 없기 때문에 양쪽 다 넣어줌
    adjL[n1].append(n2)
    adjL[n2].append(n1)
print()
# 1: 시작 정점, V 마지막 정점(정점 개수)
bfs(1, V)    # 1 2 3 4 5 7 6




# < 방문 처리로 bfs 구현하기 >
'''
# G : 그래프 정보/ v : 시작 정점 번호 / n : 정점의 개수
def bfs(G, v, n):
    # 방문 배열
    visited = [0] * (n + 1)
    q = []
    # q 에 시작점 넣은 상태로 반복 시작!
    q.append(v)
    visited[v] = 1

    # q가 비어있지 않는 동안 계속
    while q:
        t = q.pop(0)
        print(t)
        # 현재 정점 t에 연결된 모든 정점 i 탐색
        for i in G[t]:
            # i 번 정점을 방문한 적이 없다면
            if not visited[i]:
                # 다음에 방문하기 위해 큐에 넣고, 방문 처리
                q.append(i)
                visited[i] = 1


#        0    1    2    3    4    5    6    7    8    9
node = ['x', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']

# 1. 그래프 정보 주어지는데 어떻게 처리할거냐?
# 정점의 개수 V
# V = 9
# 간선의 개수 E
# E : 8
'''
'''
9 8
1 2
1 3 
1 4 
2 5 
2 6 
4 7
4 8
4 9  
'''
'''
# V 정점의 개수 / E 노드의 개수
V, E = map(int, input().split())
G = [[] for _ in range(V + 1)] # 1부터 시작
for i in range(E):
    start, to = arr = map(int, input().split())
    G[start].append(to)
    G[to].append(start)

print(G)
# bfs(node, 1, V) # ABCDEFGHI
'''


# < 큐 크기로 bfs 구현하기 >

'''
def is_valid(r, c):
    return 0 <= r < n and 0 <= c < n

# sr : 시작 행/ sc : 시작 열
def bfs(sr, sc):
    visited = [[0] * n for _ in range(n)]
    q = []
    q.append((sr, sc))
    visited[sr][sc] = 1
    day = 0    # 시작전에 하거나 반복이 끝났을 때 day += 1

    while q:
        # 원소를 반환하기 전에 현재 단계에서 큐의 원소를 몇개까지 하면 되는지
        size = len(q)
        day += 1
        for _ in range(size):

            # q의 첫번째 원소 반환
            r, c = q.pop(0)
            for i in range(n):
                for j in range(n):
                    if (i, j) == (r, c):
                        print('★', end=' ')
                    else:
                        print(maze[i][j], end=' ')
                print()
            print('==============')

            if maze[r][c] == 3:
                print(f'탈출 : {day}')
                q = [] # while 문 탈출하기 위해
                break # for 문 탈출

            dr = [0, 1, 0, -1]
            dc = [1, 0, -1, 0]

            # 현 위치 r, c에서 4 방향 탐색
            for d in range(4):
                nr, nc = r + dr[d], c + dc[d]
                if is_valid(nr, nc) and maze[nr][nc] != 1 and not visited[nr][nc]:
                    q.append((nr, nc))
                    visited[nr][nc] = 1

n = 7
maze = [[0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 0],
        [0, 1, 0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [1, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 3, 0, 0, 1],
        [0, 0, 1, 1, 1, 0, 1]]

bfs(0, 0)
'''