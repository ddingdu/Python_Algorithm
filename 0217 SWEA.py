'''  입력
3
4
5
6
'''

# 달팽이 숫자
'''
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]

    i = j = dr = 0  # 초기값 설정
    for cnt in range(1, N * N + 1):
        arr[i][j] = cnt  # 현재좌표에 숫자 기록
        ni, nj = i + di[dr], j + dj[dr]  # 이동할 위치 계산
# 출력값 실행했는데 잘못 된 값 나오면 디버깅 실행 - 18번 줄 돌려보는 거 추천

        # 이동할 위치가 범위내 and 빈칸(==0)인경우 이동
        if 0 <= ni < N and 0 <= nj < N and arr[nj][nj] == 0:
            i, j = ni, nj
        else:  # 방향을 꺽어서 이동위치 다시 계산
            dr = (dr + 1) % 4  # 0-1-2-3-1-2..
            i, j = i + di[dr], j + dj[dr]

    print(f'#{test_case}')
    for lst in arr:
        print(*lst)
'''
import sys
sys.stdin = open('../input.txt', 'r')

# 9489. 고대 유적 # 라이브 문제풀이
# (9367. 점점 커지는 당근의 개수's 가로세로 버전)

# def count(arr):
#     mx = 2
#     for lst in arr:
#         cnt = 0
#         for n in lst:
#             if n == 1:
#                 cnt += 1
#                 if mx < cnt:
#                     mx = cnt
#             else:
#                 cnt = 0
#     return mx
#
# t = int(input())
# for tc in range(1, t + 1):
#     n, m = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(n)]
#     arr_t = list(map(list, zip(*arr)))
#
#     ans = count(arr)
#     t = count(arr_t)
#     if ans < t:
#         ans = t
#     print(f'#{tc} {ans}')
'''
# 내 풀이 + 재만님 도움
t = int(input())
for tc in range(1, t + 1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    n_arr = list(map(list, zip(*arr)))

    mx_cnt = 2
    for lst in arr:
        cnt = 0
        for i in lst:
            if i == 1:     # 1 만났을 때
                cnt += 1
            else:          # 0 만났을 때
                if cnt > mx_cnt:
                    mx_cnt = cnt
                cnt = 0    # cnt 값 초기화
        if cnt > mx_cnt:   # 최댓값 저장
            mx_cnt = cnt

    n_mx_cnt = 2
    for lst in n_arr:
        n_cnt = 0
        for j in lst:
            if j == 1:
                n_cnt += 1
            else:
                if n_cnt > n_mx_cnt:
                    n_mx_cnt = n_cnt
                n_cnt = 0
        if n_cnt > n_mx_cnt:
            n_mx_cnt = n_cnt

    ans = mx_cnt
    # 가로와 세로 중 큰 값 비교해서 출력
    if mx_cnt < n_mx_cnt:
        ans = n_mx_cnt

    print(f'#{tc} {ans}')
'''
# 5432. 쇠막대기 자르기

# 레이저로 자를 때, 전체 개수 늘리면서 쌓여있는 막대 수도 줄여야겠다.
# (): 레이저, ( : 쇠막대기 왼쪽 끝, ) : 오른쪽 끝
'''
t = int(input())
for tc in range(1, t + 1):
    st = input()
    # cnt : 쌓여 있는 막대 수 ??? / ans : 잘린 조각의 총 개수
    cnt = ans = 0
    for i in range(len(st)):
        if st[i] == "(":
            cnt += 1    # 레이저로 오해
        else:   # ")" 일때, 바로 앞 기호 확인
            if st[i-1] == "(":   # "()" 레이저
                cnt -= 1    # 레이저로 오해 했던 거 빼줌 ???
                ans += cnt
            else:               # 막대기의 끝
                cnt -= 1
                ans += 1

    print(f'#{tc} {ans}')
'''
# 1859 백만 장자 프로젝트
'''
t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    lst = list(map(int, input().split()))

    i = ans = 0
    while i < n:
        # i ~ 끝까지 최대값의 index 찾기
        i_mx = i
        for j in range(i+1, n):
            if lst[i_mx] < lst[j]:
                i_mx = j
        # i ~ i_mx 까지의 최대값과의 차이 누적
        for j in range(i, i_mx):
            ans += lst[i_mx] - lst[j]
        i = i_mx + 1

    print(f'#{tc} {ans}')

# 방법 2) 뒤에서부터 확인하기
t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    # 리스트 뒤집기
    lst = list(map(int, input().split()))[::-1]

    ans = mx = 0
    for t in lst:
        if mx > t:
            # 큰 값과 작은 값 차이
            ans += mx - t
        else:
            # 큰 값 갱신
            mx = t

    print(f'#{tc} {ans}')
'''
'''
# 자기 방으로 돌아가기
t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    cnts = [0] * 200

    for _ in range(n):
        # s : 현재 방 번호, e : 돌아가야할 방 번호
        s, e = map(int, input().split())

        # start 가 end 보다 크다면, 바꿔서 저장
        if s > e:
            s, e = e, s
        # (방 번호-1)//2 : 복도 번호 인덱스
        for i in range((s-1)//2, (e-1)//2+1):
            cnts[i] += 1

    mx = 0
    for c in cnts:
        if c > mx:
            mx = c
    print(f'#{tc} {mx}')
'''
# 재미있는 오셀로 게임

# 빈 공간에 돌을 놓을 수 있음
# 자신이 놓을 돌과 자신의 돌 사이에 상대편의 돌이 있을 경우에만 돌을 놓을 수 있음, 상대편 돌을 자신의 돌로
# 가로/세로/대각선 가능

'''
T = int(input())
for test_case in range(1, T + 1):
    # N : 한 변의 길이, M : 플레이어가 돌을 놓는 횟수
    N, M = map(int, input().split())
    # arr 네방향 0으로 패딩해서 둘러쌈
    arr = [[0] * (N + 2) for _ in range(N + 2)]

    # [1] 초기 돌, 정가운데에 배치
    m = N // 2
    arr[m][m] = arr[m + 1][m + 1] = 2
    arr[m + 1][m] = arr[m][m + 1] = 1

    # [2] 흑돌 백돌 입력 받아서 처리
    for _ in range(M):
        # (si, sj) : 돌 놓을 좌표, d : 돌 색
        si, sj, d = map(int, input().split())
        arr[si][sj] = d
        # 8방향 (해당 방향으로 뻗어나가면서 처리)
        for di, dj in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):
            # 뒤집기 후보 넣어줄 리스트
            t_lst = []
            # mul 칸 만큼 뻗어 나가기 (1부터 N-1 까지)
            for mul in range(1, N):
                ni, nj = si + di * mul, sj + dj * mul
                if arr[ni][nj] == 0:  # 빈칸 범위 밖이면 중단
                    break
                elif arr[ni][nj] != d:  # d 가 아닌 다른 돌인 경우 뒤집기 후보에 추가
                    t_lst.append((ni, nj)) # 리스트에 좌표 push
                    
                else:  # d와 같은 돌이라면, 후보들을 뒤집고, 종료
                    while t_lst:
                        ti, tj = t_lst.pop()
                        arr[ti][tj] = d
                    break

    # 흑돌, 백돌 개수
    bcnt = wcnt = 0
    for lst in arr:
        # 배열 내 1이면 흑돌, 2면 백돌
        bcnt += lst.count(1)
        wcnt += lst.count(2)
    print(f'#{test_case} {bcnt} {wcnt}')
'''
'''
# 우주선 착륙2

# 예비 후보지는 8개 방향 중 사진을 찍을 수 있는 방향이 4방향 이상인 지점으로
dr = [-1, 1, 0, 0, -1, 1, 1, -1]
dc = [0, 0, -1, 1, 1, 1, -1, -1]

t = int(input())
for tc in range(1, t + 1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    # 후보지 초기화
    ans = 0

    for r in range(n):
        for c in range(m):
            # 구역번호 합 초기화
            cnt = 0
            # < 방법 1 > 8 방향 탐색
            for d in range(8):
                nr = r + dr[d]
                nc = c + dc[d]
                if 0 <= nr < n and 0 <= nc < m and arr[nr][nc] < arr[r][c]:
                    cnt += 1

            # # 구역번호 합 초기화
            # cnt = 0
            # # < 방법 2 > 3*3 배열 탐색
            # for nr in range(r-1, r+2):
            #     for nc in range(c-1, c+2):
            #         if 0 <= nr < n and 0 <= nc < m and arr[nr][nc] < arr[r][c]:
            #             cnt += 1
            # 4 곳 이상이라면 후보지에 추가
            if cnt >= 4:
                ans += 1
    print(f'#{tc} {ans}')
'''