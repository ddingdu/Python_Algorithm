import sys

sys.stdin = open("../input.txt", "r")

# 우 하 좌 상 => 0 1 2 3
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def is_valid(r, c):
    return 0 <= r < n and 0 <= c < n and not visited[r][c]


T = int(input())

for tc in range(1, T + 1):
    n = int(input())

    area = [list(map(int, input().split())) for _ in range(n)]
    # 방문 체크
    visited = [[0] * n for _ in range(n)]

    # 시작위치는 0,0
    r, c = 0, 0
    # 시작 방향은 area[0][0]
    d = area[0][0]

    # 에너지 기록
    energy = [d]

    # 더이상 움직일수 없을때까지 반복
    while True:
        # 현재 에너지를 기록
        # 이전 방향과 다를 경우에만 기록한다
        if energy[-1] != d:
            energy.append(d)

        # 다음 위치 계산
        nr = r + dr[d]
        nc = c + dc[d]

        # 다음 위치 검사해서 유효한 위치면 이동
        if is_valid(nr, nc):
            # 방문 체크
            visited[nr][nc] = 1
            # 현재 위치를 다음 위치로 바꾸기
            r, c = nr, nc
            # 방향도 다음 방향으로 바꿔준다.
            d = area[nr][nc]
        # 유효한 위치가 아니면 탐색 중단
        else:
            break

    print(f"#{tc} ", end="")
    print(*energy, sep=" ")
    # print()