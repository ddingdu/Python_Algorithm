import sys
sys.stdin = open('input.txt', 'r')
import pprint
'''
Q. 탈주범이 위치할 수 있는 장소의 개수

지도의 세로 크기 N, 가로 크기 M
맨홀 뚜껑 세로 위치 R, 가로 위치 C
탈출 후 소요된 시간 L
'''

p = { 1: [(-1,0),(1,0),(0,-1),(0,1)],
      2: [(-1,0),(1,0)],
      3: [(0,-1),(0,1)],
      4: [(-1,0),(0,1)],
      5: [(1,0),(0,1)],
      6: [(1,0),(0,-1)],
      7: [(-1,0),(0,-1)]
}

t = int(input())
for tc in range(1, t+1):
    n, m, r, c, l = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    pprint.pprint(arr)
    v = [[0] * m for _ in range(n)]
    v[r][c] = 1
    q = [(r, c)]

    cnt = 1
    while q:
        sr, sc = q.pop(0)
        for dr, dc in p[arr[sr][sc]]:
            nr, nc = sr + dr, sc + dc
            if 0 <= nr < n and 0 <= nc < m and v[nr][nc] == 0 and arr[nr][nc] and (-dr, -dc) in p[arr[nr][nc]]:
                q.append((nr, nc))
                v[nr][nc] = v[sr][sc] + 1
                if v[nr][nc] <= l:
                    cnt += 1
    print(f'시작 좌표(r, c):{(r, c)}, 제한 시간(l):{l}')
    pprint.pprint(v)
    print(f'#{tc} {cnt}')