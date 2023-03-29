import sys

sys.stdin = open("../23.03.29_분할정복/input.txt", "r")

dr = [-1, -1, -1, 0, 0, 1, 1, 1]
dc = [-1, 0, 1, -1, 1, -1, 0, 3]


def in_range(r, c):
    return 0 <= r < n and 0 <= c < n


T = int(input())

for tc in range(1, T + 1):
    n = int(input())

    mountains = [list(map(int, input().split())) for _ in range(n)]

    # 봉우리의 개수
    hill = 0

    # 최대높이, 최소높이
    max_h = 0
    min_h = 100

    # 2차원 배열 탐색 모든 위치 r,c 를 검사를 하는데 외곽은 검사할 필요가 없다(봉우리로 취급안함)
    for r in range(n):
        for c in range(n):

            # 8 방향 탐색
            for d in range(8):
                nr = r + dr[d]
                nc = c + dc[d]

                # nr , nc 가 범위 안
                if in_range(nr, nc):
                    # 내 주변 위치(nr , nc)가 현재 위치 r, c 보다 높은지 검사
                    if mountains[r][c] <= mountains[nr][nc]:
                        # 현재 위치 r,c 보다 다음 위치 nr,nc가 높거나 같으면 봉우리 아님
                        break
                # 범위밖이면 ==> 외곽이니까 탐색 중단(다음 n, r로)
                else:
                    break
            # 중간에 8방향 탐색을 그만둔적이 없다면 주변이 다 나보다 낮고, 8방향이 온전히 있는 위치
            else:
                hill += 1
                max_h = mountains[r][c] if max_h < mountains[r][c] else max_h
                min_h = mountains[r][c] if min_h > mountains[r][c] else min_h

    # # 외곽을 제외하고 r,c 검사
    # for r in range(1, n - 1):
    #     for c in range(1, n - 1):
    #
    #         # 8방향 탐색해서 나보다 높거나 같은곳 있는지만 검사
    #         for d in range(8):
    #             nr = r + dr[d]
    #             nc = c + dc[d]
    #
    #             if mountains[r][c] <= mountains[nr][nc]:
    #                 break
    #         else:
    #             hill += 1
    #             max_h = mountains[r][c] if max_h < mountains[r][c] else max_h
    #             min_h = mountains[r][c] if min_h > mountains[r][c] else min_h

    # 봉우리의 개수가 2개 이상이면 최대-최소 계산
    if hill >= 2:
        print(f"#{tc} {max_h - min_h}")
    # 봉우리의 개수가 1개 이하이면 -1 출력
    else:
        print(f"#{tc} {-1}")
