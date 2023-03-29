# Contact
# 가장 나중에 연락 받게 되는 사람 중 번호가 가장 큰 사람
'''
def bfs(s):
    q = []
    visit = [0] * 101
    ans = s    # 시작 값 넣어주기

    q.append(s)
    visit[s] = 1

    while q:
        # q 에서 한개 꺼내고, 조건 맞다면 정답처리
        c = q.pop(0)

        # 방문 기록과 비교 했을 때 더 크다면 ans 에 저장
        # 같다면 값이 더 큰 쪽을 ans 에 저장
        if visit[ans] < visit[c] or ( visit[ans] == visit[c] and ans < c ):
            ans = c

        # 인접 리스트의 c 번 리스트의 원소들 확인하기
        for next in adj[c]:
            if visit[next] == 0:
                q.append(next)
                # 몇 번만에 도착할 수 있는가
                visit[next] = visit[c] + 1
    # print(visit)
    return ans

t = 10
for tc in range(1, t+1):
    # n: 데이터 길이, s: 시작점
    n, s = map(int, input().split())
    # {from, to} 순서
    data = list(map(int, input().split()))
    # print(data)
    # 인접 리스트 ( 인원 최대 100명 )
    adj = [[] for _ in range(101)]

    for i in range(0, len(data), 2):
        # 시작, 도착 2개 씩 끊어서 받기
        start, end = data[i], data[i + 1]
        # 시작 지점을 인덱스로 하는 인접 리스트에 도착 값들 넣어주기
        adj[start].append(end)
    # print(adj)
    # 시작 위치 넣어서 함수 실행
    ans = bfs(s)
    print(f'#{tc} {ans}')
'''

import sys
sys.stdin = open('../23.03.29_분할정복/input.txt', 'r')

# 파리퇴치 3
'''
# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 대각선
dx = [-1, 1, 1, -1]
dy = [1, 1, -1, -1]

t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    # print(arr)
    fly = []

    for r in range(n):
        for c in range(n):
            cnt = arr[r][c]
            for p in range(4):
                for k in range(1, m):
                    nr, nc = r + dr[p] * k, c + dc[p] * k
                    if 0 <= nr < n and 0 <= nc < n:
                        cnt += arr[nr][nc]
                        fly.append(cnt)
    # print(fly)
    for x in range(n):
        for y in range(n):
            cnt = arr[x][y]
            for s in range(4):
                for t in range(1, m):
                    nx, ny = x + dx[s] * t, y + dy[s] * t
                    if 0 <= nx < n and 0 <= ny < n:
                        cnt += arr[nx][ny]
                        fly.append(cnt)
    ans = max(fly)
    print(f'#{tc} {ans}')
'''
# 오셀로 게임
'''
t = int(input())
for tc in range(1, t + 1):
    # n : 한 변의 길이, m : 플레이어가 돌을 놓는 횟수
    n, m = map(int, input().split())
    # arr 네방향 0으로 패딩해서 둘러쌈
    arr = [[0] * (n + 2) for _ in range(n + 2)]

    # 돌 세팅, 배열 가운데에 배치
    c = n // 2
    arr[c][c] = arr[c+1][c+1] = 2
    arr[c+1][c] = arr[c][c+1] = 1

    for _ in range(m):
        # 돌 놓을 좌표 (i, j), d: 돌 색 (1: 흑돌, 2: 백돌)
        i, j, d = map(int, input().split())
        arr[i][j] = d
        for di, dj in ((-1,-1), (-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1)):
            turn_ls = []    # 뒤집을 후보 넣어줄 리스트
            for x in range(1, n):    # 1 부터 (n-1)까지 뻗어 나가기
                ni, nj = i + di * x, j + dj * x

                if arr[ni][nj] == 0:
                    break
                # d 와 다론 돌이라면 뒤집을 후보에 추가
                elif arr[ni][nj] != d:
                    turn_ls.append((ni, nj))    # 리스트에 좌표 push

                else:    # d 와 같은 돌이라면
                    while turn_ls:  # 후보 리스트 값이 없을 때까지 반복하다가 종료
                        # 마지막 후보부터 꺼내서 같은 돌로 바꾸기(뒤집기)
                        ti, tj = turn_ls.pop()
                        arr[ti][tj] = d
                    break

    black = white = 0
    for lst in arr:
        black += lst.count(1)
        white += lst.count(2)
    print(f'#{tc} {black} {white}')
'''
# 오목판정

t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    for _ in range(n):
        text = [list(map(int, input().split())) for _ in range(n)]





















