'''
1 이동 가능
0 이동 불가
(1,1)출발 (n, m)도착 최소 칸 수 (시작,도착 칸 포함)

상하좌우 탐색
v 빼와서 위치 찾기
1이면 이동, v 기록
'''

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
def sovle(si, sj):
    q = [(si, sj)]
    v = [[0] * (m + 1)] + [[0] * (m + 1) for _ in range(n)]
    v[si][sj] = 1

    while q:
        ci, cj = q.pop(0)
        if (ci, cj) == (n, m):
            return v[n][m]

        for d in range(4):
            ni, nj = ci + dr[d], cj + dc[d]
            if 0 <= ni < n and 0 <= nj < m and v[ni][nj] == 0 and arr[ni][nj] == 1:
                q.append((ni, nj))
                v[ni][nj] = v[ci][cj] + 1

# n: 세로, m: 가로
n, m = map(int, input().split())
arr = [[0] * (m+1)] + [[0] + list(input()) for _ in range(n)]
ans = sovle(1, 1)
print(ans)
'''
4 6
101111
101010
101011
111011

15
'''