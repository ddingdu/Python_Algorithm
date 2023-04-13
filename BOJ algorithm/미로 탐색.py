'''
1 이동 가능
0 이동 불가
(1,1)출발 (n, m)도착 최소 칸 수 (시작,도착 칸 포함)

상하좌우 탐색
v 빼와서 위치 찾기
1이면 이동, v 기록
'''


def sovle(si, sj):
    # q에 시작 좌표 넣기
    q = [(si, sj)]
    # 배열 크기와 같은 방문 배열
    v = [[0] * m for _ in range(n)]
    # 시작 좌표 방문처리
    v[si][sj] = 1

    while q:
        # q에서 꺼낸 값 현 위치로 설정
        ci, cj = q.pop(0)

        ''' 디버깅 코드
                # print("아래는 v 배열이 돌아가는 디버깅용 코드입니다.")
                # print(f"ci : {ci}, cj : {cj} 일때\n")
                print((ci, cj))
                for t in range(n+1):
                    print(v[t])

                # print("\n아래는 arr 맵입니다.")
                print()
                for t in range(n+1):
                    print(arr[t])

                print('======================')
        '''

        # 현 위치가 도착 좌표와 같다면, 방문 배열 값 출력
        if (ci, cj) == (n - 1, m - 1):
            return v[n - 1][m - 1]

        # 4방향 탐색하면서 다음 좌표 정하기
        for d in range(4):
            ni, nj = ci + dr[d], cj + dc[d]
            # 범위가 유효(패딩해서 +1)하고, 방문하지 않았고, 길이라면
            if 0 <= ni < n and 0 <= nj < m and v[ni][nj] == 0 and arr[ni][nj] == 1:
                # q에 다음 좌표 넣기
                q.append((ni, nj))
                # 방문 배열에 지금까지 지나온 거리(현재까지 더해진 값) +1 해서 저장
                v[ni][nj] = v[ci][cj] + 1


# n: 세로, m: 가로
n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

ans = sovle(0, 0)
print(ans)

'''
4 6
101111
101010
101011
111011

15
'''