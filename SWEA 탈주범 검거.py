import sys
sys.stdin = open('input.txt', 'r')

'''
Q. 탈주범이 위치할 수 있는 장소의 개수

지도의 세로 크기 N, 가로 크기 M
맨홀 뚜껑 세로 위치 R, 가로 위치 C
탈출 후 소요된 시간 L
'''
# 상하좌우
P = [[0,0,0,0], [1,1,1,1], [1,1,0,0], [0,0,1,1], [1,0,0,1], [0,1,0,1], [0,1,1,0], [1,0,1,0]]
opp = [1, 0, 3, 2]
di, dj = [-1,1,0,0], [0,0,-1,1]
def bfs(si, sj):
    q = []
    v = [[0] * M for _ in range(N)]
    cnt = 0

    q.append((si, sj))
    v[si][sj] = 1
    cnt += 1

    while q:
        ci, cj = q.pop(0)
        if v[ci][cj] == L:
            return cnt

        # 4방향 범위내
        for d in range(4):
            ni, nj = ci + di[d], cj + dj[d]
            if 0 <= ni < N and 0 <= nj < M and v[ni][nj] == 0 and P[arr[ci][cj]][d] == 1 and P[arr[ni][nj]][opp[d]] == 1:
                q.append((ni, nj))
                v[ni][nj] = v[ci][cj] + 1
                cnt += 1
    return cnt

T = int(input())
for tc in range(1, T+1):
    # 세로/가로/세로/가로/소요시간
    N, M, R, C, L  = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = bfs(R, C)
    print(f'#{tc} {ans}')