
# 우하좌상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    # 우, 하, 좌, 상
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    # 출발 좌표
    r, c = 0, 0
    d = 0
    for i in range(1, N * N + 1):
        arr[r][c] = i
        nr = r + dr[d]
        nc = c + dc[d]

        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 0:
            r, c = nr, nc
        else:
            d += 1
            if d == 4:
                d = 0
            r, c = r + dr[d], c + dc[d]
    print(f'#{tc}')
    for p in range(N):
        print(*arr[p])


