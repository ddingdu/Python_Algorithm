import sys
sys.stdin = open('../input.txt', 'r')

# 농작물 수확하기
'''
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]
    farm = 0

    # 긴 대각선 구하기
    x, y = n // 2, 0    # 시작점 설정하기
    for _ in range(n // 2+1):
        farm += arr[x][y]    # 시작 값 더하기

        # 오른쪽 아래 대각선으로 이동하면서 더해주기
        di, dj = 1, 1
        for m in range(1, n//2 + 1):
            ni, nj = x + di * m, y + dj * m
            farm += arr[ni][nj]

        # 시작점 바꿔주기
        x, y = x - 1, y + 1

    # 짧은 대각선 구하기
    r, c = n // 2, 1    # 시작점 설정하기
    for _ in range(n // 2):
        farm += arr[r][c]    # 시작 값 더하기

        # 오른쪽 아래 대각선으로 이동하면서 더해주기
        di, dj = 1, 1
        for m in range(1, n//2):
            ni, nj = r + di * m, c + dj * m
            farm += arr[ni][nj]

        # 시작점 바꿔주기
        r, c = r - 1, c + 1

    print(f'#{tc} {farm}')
'''
'''
# < 지혜 풀이 >
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    cost = 0
    # 맨 윗칸의 중간에서부터 시작
    sj = ej = N//2

    # i(행) 는 배열의 행인덱스만큼 증가
    for i in range(N):
        # j는 시작지점과 끝지점을 만들어서 범위
        for j in range(sj, ej+1):
            cost += arr[i][j]

        # i가 중간 위쪽에 있을 때
        if i < N//2:
            sj -= 1
            ej += 1
        # i가 중간 아랫쪽에 있을 때
        else:
            sj += 1
            ej -= 1

    print(f"#{tc} {cost}")

# < 금규님 풀이 >
T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    farm = [list(map(int, input())) for _ in range(n)]

    cnt = 0
    for i in range(n):
        for j in range(abs(n // 2 - i), n - abs(n // 2 - i)):
            cnt += farm[i][j]

    print(f"#{tc} {cnt}")
'''

# 오목판정

di = [-1, 0, 1, 1]
dj = [1, 1, 1, 0]

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = ['.' * (n+2)] + ['.' + input() + '.' for _ in range(n)] + ['.' * (n+2)]
    ans = 'NO'

    for i in range(1, n+1):
        for j in range(1, n+1):
            for d in range(4):
                for m in range(5):
                    ni, nj = i + di[d] * m, j + dj[d] * m
                    if arr[ni][nj] != 'o':
                        break
                else:
                    ans = 'YES'
    print(f'#{tc} {ans}')
































