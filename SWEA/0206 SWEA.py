# # 부분 집합의 합
#
# T = int(input())
#
# for tc in range(1, T+1):
#     # N : 원소 개수, K : 원소 합
#     N, K = map(int, input().split())
#     A = list(range(1, 13))
#     cnt = 0
#     # 모든 부분 집합 만들기
#     for i in range(1 << 12):
#         sub_set = []
#         sum_v = 0
#         for j in range(12):
#             if i & (1 << j):
#                 sub_set.append(A[j])
#                 sum_v += A[j]
#         # 부분 집합 원소의 개수가 N이고, 합이 K이면 cnt + 1
#         if len(sub_set) == N and sum_v == K:
#             cnt += 1
#     print(f'#{tc} {cnt}')
# (교수님 풀이)
T = int(input())

arr = [i for i in range(1, 13)]
N = 12
for tc in range(1, T+1):
    N, K = map(int, input().split())
    answer = 0
    # 부분 집합의 총 개수만큼 반복 ==> 2^N
    for i in range(1 << N):
        # i 번째 부분 집합의 합이 K이고, 개수가 N인지 확인
        subset_sum = 0
        subset_count = 0
        # i 번째 부분 집합이 j번째 원소를 포함하는지 검사
        for j in range(N):
            if i & (1 << j):
                subset_sum += arr[j]
                subset_count += 1
        # N, K 검사
        if subset_count == N and subset_sum == K:
            answer += 1
    print(f'#{tc} {answer}')

'''
# # N개 원소를 가진 부분 집합 개수 찾기
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     A = list(range(1, 13))
#     cnt = 0
#     for i in range(1 << 12):
#         sub_set = []
#         for j in range(12):
#             if i & (1 << j):
#                 sub_set.append(A[j])
#         if len(sub_set) == N:
#             cnt += 1
#     print(f'#{tc} {cnt}')
'''


# 16260 색칠하기
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [[0] * 10 for _ in range(10)]
#     cnt = 0
#     for _ in range(N):
#         r1, c1, r2, c2, color = map(int, input().split())
#         for i in range(r1, r2+1):
#             for j in range(c1, c2+1):
#                 if color == 1:
#                     arr[i][j] += 1
#                 elif color == 2:
#                     arr[i][j] += 2
#     for i in range(10):
#         for j in range(10):
#             if arr[i][j] == 3:
#                 cnt += 1
#     print(f"#{tc} {cnt}")

# (교수님 풀이)
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     paper = [[0] * 10 for _ in range(10)]
#     purple_cnt = 0 # 겹친 칸 수
#     # N 번 색칠 처리
#     for i in range(N):
#         from_i, from_j, to_i, to_j, color = map(int, input().split())
#
#         for i in range(from_i, to_i + 1):
#             for j in range(from_j, to_j + 1):
#                 if paper[i][j] == 0:
#                     paper[i][j] = color
#                 else:
#                     purple_cnt += 1
#     print(f"#{tc} {purple_cnt}")

# 풍선팡2
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # 태성풀이
    NM = [list(map(int, input().split())) for _ in range(N)]
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    max_val = 0
    for r in range(N):
        for c in range(M):
            balloon_kill = NM[r][c]
            for idx in range(4):
                nx = c + dx[idx]
                ny = r + dy[idx]
                if M - 1 >= nx >= 0 and N - 1 >= ny >= 0:
                    balloon_kill += NM[ny][nx]
            if balloon_kill > max_val:
                max_val = balloon_kill
    print(f"#{tc} {max_val}")

    #교수님풀이
T = int(input())

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 범위 검사하는 함수
def is_valid(r, c):
    return 0 <= r < n and 0 <= c < m

for tc in range(1, T + 1):
    n, m = map(int, input().split())
    # 풍선 정보
    arr = [list(map(int, input().split())) for _ in range(n)]
    max_cnt = 0

    # 모든 풍선 다 터뜨려보고 최대값 구하기
    for r in range(n):
        for c in range(m):
            # 현재 꽃가루 수 + 상하좌우 꽃가루 수
            cnt = arr[r][c]
            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]
                # 다음 위치가 배열의 범위를 벗어나지 않는지 꼭 검사하기
                if is_valid(nr, nc):
                    cnt += arr[nr][nc]

            if max_cnt < cnt:
                max_cnt = cnt
    print(f"#{tc} {max_cnt}")

# 1209 Sum
T = int(input())
arr = [[0]*100 for _ in range(100)]
T = 10

# input 값 100x100으로 어떻게 쪼개지?

# 행열
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
# 대각선
dx = [-1, 1, 1, -1]
dy = [1, 1, -1, -1]

row_sum = 0
col_sum = 0
d_sum = 0

for tc in range(1, T + 1):
    nums = map(int, input().split())

    # 행의 합
    for i in range(100):
        for j in range(100):

    # 열의 합

    # 대각선의 합







