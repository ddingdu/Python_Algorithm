import sys
sys.stdin = open('../23.03.29_분할정복/input.txt', 'r')

# 과목 1번 hill
'''
dr = [-1, -1, -1, 0, 0, 1, 1, 1]
dc = [-1, 0, 1, -1, 1, -1, 0, 1]

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    hill = []
    ans = 0

    for r in range(1, n-1):
        for c in range(1, n-1):
            # 여기에 빈리스트 넣으면 안되는 이유??
            for d in range(8):
                nr, nc = r + dr[d], c + dc[d]
                if arr[nr][nc] == arr[r][c]:    # 봉우리랑 높이 같을 때
                    break
            if arr[nr][nc] < arr[r][c]:
                hill.append(arr[r][c])
    print(hill)
    if len(hill) <= 1:
        ans = -1
    else:
        ans = max(hill) - min(hill)
    print(f'#{tc} {ans}')
'''

# 과목 2번 energy
'''
# 우 하 좌 상 ==> 0 1 2 3
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visit = [[0] * n for _ in range(n)]

    r, c = 0, 0    # 시작 좌표
    d = arr[0][0]    # 방향 번호 기록
    energy = [d]    # 출력할 방향 리스트에 시작 번호 넣기

    while True:    # 더이상 움직일수 없을때까지 반복
        if energy[-1] != d:    # 직전 방향과 다르다면 출력할 리스트에 남기기
            energy.append(d)
        nr, nc = r + dr[d], c + dc[d]    # 다음 좌표 설정
        if 0 <= nr < n and 0 <= nc < n and not visit[nr][nc]:
            visit[nr][nc] = 1    # 방문 기록
            r, c = nr, nc    # 다음 좌표로 설정
            d = arr[nr][nc]    # 다음 방향 저장
        else:
            break
    print(f'#{tc}', *energy)
'''

# 오목 판정
'''
4
5
....o
...o.
..o..
.o...
o....
5
...o.
ooooo
...o.
...o.
.....
5
.o.oo
oo.oo
.oo..
.o...
.o...
5
.o.o.
o.o.o
.o.o.
o.o.o
.o.o.
'''

'''
# 오목판정
# 1. 배열 4면 '.'으로 패딩 둘러주기
# 2. 정답 초기 값 'NO' 로 설정
# 3. 1부터 n까지 반복하면서 탐색 시작
# 4. 4방향 반복하기
# 5. 5칸 뻗어나가면서 확인하기 위해 새로운 위치 설정
# 6. 뻗어가면서 확인하다가 'o' 아니면 break
# 7. 5칸 다 확인했는데 이상 없으면 'YES' (for-else)

di = [-1, 0, 1, 1]
dj = [1, 1, 1, 0]

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    # 4면 패딩 둘러주기
    arr = ['.' * (n+2)] + ['.' + input() + '.' for _ in range(n)] + ['.' * (n+2)]
    ans = 'NO'

    # 패딩 둘러줬으므로 1 부터 n까지 확인
    for i in range(1, n+1):
        for j in range(1, n+1):
            for d in range(4):    # 4방향 탐색
                for m in range(5):    # 5칸 뻗어나가면서 확인하기
                    ni, nj = i + di[d] * m, j + dj[d] * m
                    # 뻗어가며 확인하다 돌 없으면 중단
                    if arr[ni][nj] != 'o':
                        break
                # for-else: for 문 돌면서 중간에 break 로 끊기지 않고 끝까지 수행 되었을 때 실행하는 코드
                else:    # 5칸 확인 했는데 다 돌이면 YES
                    ans = 'YES'
    print(f'#{tc} {ans}')

'''

# 스도쿠
'''
t = int(input())
for tc in range(1, t+1):
    n = 9
    arr = [list(map(int, input().split())) for _ in range(n)]
    n_arr = list(zip(*arr))    # 전치행렬
    ans = 1
    # 가로 검사
    for num in arr:
        if len(set(num)) != 9:
            ans = 0
    # 세로 검사
    for num in n_arr:
        if len(set(num)) != 9:
            ans = 0
    # 3*3 작은 네모 검사
    for i in (0, 3, 6):
        for j in (0, 3, 6):
            num = arr[i][j:j+3] + arr[i+1][j:j+3] + arr[i+2][j:j+3]
            if len(set(num)) != 9:
                ans = 0

    print(f'#{tc} {ans}')
'''
# 오셀로

# 1. 배열 0으로 채우고 4면 패딩처리
# 2. 탐색 시작 전, 중앙에 흑/백 2개씩 교차 놓기
# 3. 돌 놓는 횟수 만큼 반복
# 4. 좌표랑 돌 받고, 시작 위치에 돌 놓기
# 5. 8 방향 탐색
# 6. 후보 리스트 만들고 1부터 (n-1)까지 뻗어가기
# 7. 탐색 위치 설정, 빈자리면 break/색 다르면 좌표 push/색 같으면 pop 하고 뒤집기

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

t = int(input())
for tc in range(1, t+1):
    # n: 변 길이, m: 돌 놓는 횟수
    n, m = map(int, input().split())

    # 0 으로 채워진 배열 4면 패딩처리
    arr = [[0] * (n + 2) for _ in range(n + 2)]
    # (탐색 시작 전) 중앙에 흑돌 백돌 2개씩 교차해서 놓기
    c = n // 2
    arr[c][c] = arr[c + 1][c + 1] = 2
    arr[c + 1][c] = arr[c][c + 1] = 1

    for _ in range(m):
        # i, j: 좌표 , s: 돌 색깔 (1: blk, 2: wht)
        i, j, s = map(int, input().split())
        arr[i][j] = s   # 시작점 돌 놓기

        for d in range(8):  # 8방향 탐색

            turn_ls = []    # 후보 넣을 리스트
            for x in range(1, n):   # 1부터 (n-1)까지 뻗어가기

                ni, nj = i + dx[d] * x, j + dy[d] * x
                # 탐색한 위치가 빈자리라면 중단
                if arr[ni][nj] == 0:
                    break
                # 돌 색깔 다르다면 후보 리스트에 좌표 push
                elif arr[ni][nj] != s:
                    turn_ls.append((ni, nj))
                # 돌 색깔 같다면 후보 리스트의 좌표 pop 해서 뒤집기(같은 색으로 바꿔주기)
                else:
                    while turn_ls:  # 후보가 있는 동안
                        ti, tj = turn_ls.pop()
                        arr[ti][tj] = s
                    break   # 범위 벗어나지 않게 중단

    blk = wht = 0
    for lst in arr:
        blk += lst.count(1)
        wht += lst.count(2)
    print(f'#{tc} {blk} {wht}')

# 간단한 압축 풀기
'''
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    line = ''
    for _ in range(n):
        alpha, num = input().split()
        line += alpha * int(num)

    print(f'#{tc}')
    for i in range(0, len(line), 10):
        print(line[i:i+10])
'''