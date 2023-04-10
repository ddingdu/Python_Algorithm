import sys
sys.stdin = open('../input.txt', 'r')

'''
완전 탐색
1. 배열 입력 받으면서 최고 높이 찾기
2. 전체 배열 살펴보면서 최고 높이 값의 좌표 저장
3. 최고 높이 좌표에서 탐색 시작, 1부터 한칸씩 깎아보고 재귀돌려보기 (k까지)
4. 재귀 돌린 후 높이 복구
'''

def solve(sx, sy, changed_map, cnt):
    global result

    # 가장 긴 길이를 정답으로
    result = max(result, cnt)

    # 4방향 다음 좌표 설정하기
    for d in range(4):
        nx, ny = sx + dx[d], sy + dy[d]

        # 유효한 범위, 깎은 지도의 다음 위치가 현 위치 보다 작다면 재귀
        if 0 <= nx < n and 0 <= ny < n and changed_map[nx][ny] < changed_map[sx][sy]:
            # 다음 좌표, 깎은 지도, 길이 +1
            solve(nx, ny, changed_map, cnt + 1)

t = int(input())
for tc in range(1, t+1):
    n, k = map(int, input().split())
    arr = []
    top_lst = [] # 최고 높이 좌표
    mx_h = 0     # 최고 높이
    result = 0   # 최대 길이를 비교하기 위함

    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 배열 입력 받으면서 최고 높이 찾기
    for _ in range(n):
        a = list(map(int, input().split()))
        mx_h = max(mx_h, max(a))
        arr.append(a)

    # 배열 전체 탐색하면서 최고 높이의 좌표들 저장
    for i in range(n):
        for j in range(n):
            if arr[i][j] == mx_h:
                top_lst.append((i, j))

    # 최고 높이 위치부터 시작해서 전체 탐색
    for x, y in top_lst:
        for i in range(n):
            for j in range(n):
                # 배열 한 칸씩 높이를 1부터 k까지 깎아보기
                for depth in range(1, k+1):
                    arr[i][j] -= depth
                    solve(x, y, arr, 1)
                    # 함수 실행 후, 지도 복구
                    arr[i][j] += depth

    print(f'#{tc} {result}')