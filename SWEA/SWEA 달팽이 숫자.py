# n*n 까지의 숫자가 1부터 시계방향

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [[0] * n for _ in range(n)]
    # 우하좌상
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    # 시작점 및 방향
    si = sj = d = 0

    for i in range(1, n*n+1):
        arr[si][sj] = i
        nr, nc = si + di[d], sj + dj[d]
        if 0 <= nr < n and 0 <= nc < n and arr[nr][nc] == 0:
            si, sj = nr, nc
        else:
            d += 1
            if d == 4:
                d = 0
            si, sj = si + di[d], sj + dj[d]

    print(f'#{tc}')
    for lst in range(n):
        print(*arr[lst])

