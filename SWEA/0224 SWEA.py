# BFS
# [참고 BFS 알고리즘]
# def BFS(G, v, n):
#     visited = [0] * (n+1)
#     queue = []
#     visited[v] = 1
#     while queue :
#         t = queue.pop(0)
#         visit(t)
#         for i in G[t]:
#             if not visited[i]:
#                 queue.append(i)
#                 visited[i] = visited[n] + 1

# # [BFS template]
# def bfs(si, sj, ei, ej):
#     q = []
#     v = [[0] * N for _ in range(N)]
#
#     q.append((si, sj, 0))
#     v[si][sj] = 1
#
#     while q:
#         cj, cj, d = q.pop(0)
#         if ci == ej and cj == ej:
#             return d - 1
#         for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
#             ni, nj = ci + di, cj + dj
#             if 0 <= ni < N and 0 <= nj < N and v[ni][nj] == 0 and arr[ni][nj] != '1':
#                 q.append((si, sj, 0))
#                 v[si][sj] = 1
#     return 0


import sys
sys.stdin = open('../input.txt', 'r')

# Contact

# 가장 나중에 연락 받게 되는 사람 중 번호가 가장 큰 사람
def bfs(s):
    q = []
    v = [0] * 101
    ans = s    # 시작값 넣어주기

    q.append(s)
    v[s] = 1

    while q:
        # q에서 한개 꺼내고, 정답처리
        c = q.pop(0)
        if v[ans] < v[c] or ( v[ans] == v[c] and ans < c ):
            ans = c

        # 3. current(c) 현재 연결방향 반복처리, next(n)
        for n in adj[c]:
            if v[n] == 0:
                q.append(n)
                v[n] = v[c] + 1
    return ans

t = 10
for tc in range(1, t + 1):
    n, s = map(int, input().split())
    lst = list(map(int, input().split()))
    # 인접리스트에 연결 저장
    adj = [[] for _ in range(101)]
    for i in range(0, len(lst), 2):
        # 2개 씩 끊어서 저장
        start, end = lst[i], lst[i + 1]
        adj[start].append(end)

    ans = bfs(s)
    print(f'#{tc} {ans}')


# 정사각형방
# 이동할 수 있는 방의 개수가 최대인 방이 여럿이라면 그 중에서 적힌 수가 가장 작은 것을 출력

'''
def bfs(si, sj):
    q = []
    alst = []

    q.append((si, sj))
    v[si][sj] = 1
    alst.append(arr[si][sj])

    while q:
        ci, cj = q.pop(0)
        # 4방향, 미방문, 조건 맞으면!! (1차이)
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < n and 0 <= nj < n and v[ni][nj] == 0 and abs(arr[ci][cj] - arr[ni][nj]) == 1:
                q.append((ni, nj))
                v[ni][nj] = 1
                alst.append(arr[ni][nj])

    return min(alst), len(alst)

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    v = [[0] * n for _ in range(n)]
    ans, cnt = n * n, 0
    for si in range(n):
        for sj in range(n):
            if v[si][sj] == 0:
                t, tcnt = bfs(si, sj)
                if cnt < tcnt or ( cnt == tcnt and ans > t ):
                    ans, cnt = t, tcnt
    print(f'#{tc} {ans} {cnt}')
'''

# 탈주범 검거

'''
# 파이프
p = [[], [0,1,2,3], [0,1], [2, 3], [0, 3], [1, 3], [1, 2], [0, 2]]
opp = {0:1, 1:0, 2:3, 3:2}
# 상하좌우
di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]

def bfs(si, sj, l):
    q = []
    v = [[0] * m for _ in range(n)]   # 가로 세로 다를때 특히 주의 !!

    q.append((si, sj))
    v[si][sj] = 1
    cnt = 1

    while q:
        ci, cj = q.pop(0)
        if v[ci][cj] == l:
            return cnt

        # 현위치 파이프에 연결된
        for d in p[arr[ci][cj]]:
            ni, nj = ci + di[d], cj + dj[d]
            # 내 방향으로 연결된 파이프가 이동할 방향에 있다면
            if 0 <= ni < n and 0 <= nj < m and v[ni][nj] == 0 and opp[d] in p[arr[ni][nj]]:
                q.append((ni, nj))
                # 얼마나 뻗어나갔는지 볼 수 있도록
                v[ni][nj] = v[ci][cj] + 1
                cnt += 1
    # 이경우 -1 리턴? X
    # 공간이 좁아서 L일 전에 모두 방문!
    return cnt

t = int(input())
for tc in range(1, t+1):
    # n: 세로, m:가로, r: 맨홀 세로 위치, c: 맨홀 가로 위치, l: 탈출 후 소요시간
    n, m, r, c, l = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    ans = bfs(r, c, l)
    print(f'#{tc} {ans}')
'''

# 홈 방범 서비스

# 보안회사가 손해를 보지 않고(같거나 크면) 서비스 가능한 최대 집의 수
# [ 방법 1. 전체 순회 ] <IM> 달팽이숫자, 농작물 수확하기
'''
def solve_loop():
    mx = 0
    # 가능한 모든 시작위치
    for si in range(n):
        for sj in range(n):
            for k in range(1, 2 * n):
                cnt = 0
                for i in range(si - k + 1, si + k):
                    t = abs(si - i)
                    for j in range(sj - k + 1 + t, sj + k - t):
                        if 0 <= i < n and 0 <= j < n:
                            # 집 위치 더하기 (집이 1이니 집 개수 추가)
                            cnt += arr[i][j]
                # 운영 비용 보다 수익이 크거나 같다면 정답 갱신
                # (들여쓰기 위치 : 마지막 k 값에서 갱신)
                if ((k*k) + (k-1) * (k-1)) <= cnt * m:
                    mx = max(mx, cnt)
    return mx

t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    ans = solve_loop()
    print(f'#{tc} {ans}')
'''

# [ 방법 2. BFS]
'''
cost = [((k*k)+(k-1)*(k-1)) for k in range(40)]

def solve_bfs():
    mx = 0
    for si in range(n):
        for sj in range(n): # 가능한 모든 시작위치
            mx = max(mx, bfs(si,sj))
    return mx

def bfs(si,sj):
    q = []
    v = [[0]*n for _ in range(n)]
    old = 0
    mx = 0
  
    q.append((si,sj))
    v[si][sj]=1
    cnt = arr[si][sj]   # 시작좌표가 집이면 1, 아니면 0
  
    while q:
        ci,cj = q.pop(0)
        if old != v[ci][cj]:    # k값이 달라진경우(방문한 경우)
            old = v[ci][cj]
            if cost[v[ci][cj]]<=cnt * m:
                mx = max(mx, cnt)
  
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj = ci+di, cj+dj
            if 0<=ni<n and 0<=nj<n and v[ni][nj]==0:
                q.append((ni,nj))
                v[ni][nj]=v[ci][cj]+1
                cnt += arr[ni][nj]
    return mx

t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    ans = solve_bfs()
    print(f'#{tc} {ans}')
'''

# [ 방법 3. Greedy 규칙성 아이디어 ]
'''
cost = [((k*k)+(k-1)*(k-1)) for k in range(40)]

def solve_idea():
    mx = 0
    home = []
    # 가능한 모든 시작위치
    for si in range(n):
        for sj in range(n):
            # 집의 모든 위치 저장
            if arr[si][sj] == 1:
                home.append((si, sj))

    #  각 기준 위치에서 거리별 집의 개수 누적하기
    for si in range(n):
        for sj in range(n):
            dist = [0] * 40
            # 거리(t)별 집 위치를 누적
            for ti, tj in home:
                # 같은 위치에 있으면 k 가 1이기 때문에 + 1
                t = abs(si - ti) + abs(sj - tj) + 1
                dist[t] += 1

            for k in range(1, 40): # k 범위
                dist[k] += dist[k - 1]
                if cost[k] <= dist[k] * m:
                    mx = max(mx, dist[k]) # dist[k]가 카운트
    return mx

t = int(input())
for tc in range(1, t + 1):
    n, m = map(int, input().split())    # m: 비용
    arr = [list(map(int, input().split())) for _ in range(n)]
    ans = solve_idea()
    print(f'#{tc} {ans}')
'''

# 사칙연산 <과제>
'''
# 후위순회
def postorder(t):   # t: 현재 노드 번호

    # t 노드가 숫자인 경우( 단말노드 )
    if node[t].isdigit():
        return int(node[t])

    # t 노드가 연산자인 경우 후위순회
    else:
        left = postorder(cleft[t])
        right = postorder(cright[t])

        # isdigit() 써야하기 때문에 문자열로 저장
        if node[t] == '+':
            node[t] = str(left + right)
        elif node[t] == '-':
            node[t] = str(left - right)
        elif node[t] == '*':
            node[t] = str(left * right)
        elif node[t] == '/':
            node[t] = str(left // right)

        # node[t] 에 저장은 문자열, 리턴은 숫자값으로 (사칙연산 위해)
        return int(node[t])

t = 10
for tc in range(1, t + 1):
    n = int(input())

    # 자식 정보 (완전이진트리 아니기 때문에 왼쪽, 오른쪽 나눠줌)
    cleft = [0] * (n + 1)
    cright = [0] * (n + 1)

    # 인덱스에 저장된 값 또는 연산자
    node = [0] * (n + 1)

    for i in range(n):
        info = input().split()

        # 해당 노드의 인덱스는 첫 번째칸, 인덱스로 쓰려고 숫자로 바꿔줌
        idx = int(info[0])

        # 값이 숫자면
        if info[1].isdigit():
            node[idx] = info[1]

        # 값이 연산자면 왼쪽, 오른쪽 자식 정보 저장
        else:
            node[idx] = info[1]
            cleft[idx] = int(info[2])
            cright[idx] = int(info[3])

    print(f'#{tc} {postorder(1)}')
'''