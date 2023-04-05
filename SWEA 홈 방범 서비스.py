import sys
sys.stdin = open('input.txt', 'r')

# 손해를 보지 않고(같거나 큰) 서비스 가능한 최대 집의 수

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def is_valid(r, c):
    return 0 <= r < n and 0 <= c < n

def bfs(r, c, k):
    v = [[0] * n for _ in range(n)]
    q = [(r, c)]
    v[r][c] = 1

    h_cnt = 0

    while q:
        r, c = q.pop(0)
        if v[r][c] > k:
            break
        if arr[r][c] == 1:
            h_cnt += 1
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if is_valid(nr, nc) and v[nr][nc] == 0:
                q.append((nr, nc))
                v[nr][nc] = v[r][c] + 1
    cost = m * h_cnt - k ** 2 - (k - 1) ** 2

    return cost, h_cnt

T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    max_cnt = 0

    for r in range(n):
        for c in range(n):
            for k in range(1, n+3):
                cost, cnt = bfs(r, c, k)
                if cost < 0:
                    continue
                # print(r, c, k, cost, cnt)
                max_cnt = max(cnt, max_cnt)

    print(f"#{tc} {max_cnt}")