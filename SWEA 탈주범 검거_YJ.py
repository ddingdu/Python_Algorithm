import sys
sys.stdin = open('input.txt', 'r')

dist = {1: [(-1, 0), (1, 0), (0, -1), (0, 1)],
        2: [(-1, 0), (1, 0)],
        3: [(0, -1), (0, 1)],
        4: [(-1, 0), (0, 1)],
        5: [(1, 0), (0, 1)],
        6: [(1, 0), (0, -1)],
        7: [(-1, 0), (0, -1)]}

T = int(input())
for tc in range(1, T+1):
    # R:맨홀 세로, C:맨홀 가로, L:탈출 소요시간
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(arr)
    v = [[0] * M for _ in range(N)]
    v[R][C] = 1
    q = [(R, C)]

    cnt = 1
    while q:
        R, C = q.pop(0)
        for di, dj in dist[arr[R][C]]:
            nr, nc = R + di, C + dj
            if 0 <= nr < N and 0 <= nc < M and not v[nr][nc] and arr[nr][nc] and (-di, -dj) in dist[arr[nr][nc]] :
                q.append((nr, nc))
                v[nr][nc] = v[R][C] + 1

                if v[nr][nc] <= L:
                    cnt += 1
    print(v)

    print(f'#{tc} {cnt}')