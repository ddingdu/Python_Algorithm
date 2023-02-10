# 1979 어디에 단어가 들어갈 수 있을까? - 전치행렬/경계 값 0
'''
def cnt(arr):
    answer = 0
    for lst in arr:
        count = 0
        for n in lst:
            if n == 1:  # 1 : 단어를 넣을 수 있는 공백
                count += 1
            else:   # 공백 없으면 길이 같을 때 세주기
                if count == k:
                    answer += 1
                # 반복문 돌기 전에 초기화
                count = 0
    return answer

t = int(input())
for tc in range(1, t+1):
    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) + [0] for _ in range(n)] + [[0] * (n + 1)]
    n_arr = [[0] * (n + 1) for _ in range(n)] + [[0] * (n + 1)]

    for i in range(n):
        for j in range(n):
            if i <= j:  # 대각선 포함 바꿔주기
                n_arr[i][j], n_arr[j][i] = arr[j][i], arr[i][j]

    # n_arr = list(map(list, zip(*arr)))  # zip()함수 사용해서 전치행렬

    ans = cnt(arr) + cnt(n_arr)
    print(f'#{tc} {ans}')
'''
# 1946 간단한 압축 풀기
'''
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    ans = ''

    for _ in range(n):
        a, number = input().split()
        ans += a * int(number)

    print(f'#{tc}')

    for i in range(0, len(ans), 10):
        print(ans[i:i+10])

    # for i in range((len(s) // 10) + 1): # 몫, 3줄 / i = 0,1,2
    #     start = i * 10
    #     end = (i + 1) * 10
    #     if end <= len(s):
    #         print(s[start:end])
    #     else:
    #         print(s[start:])
'''
# 회문 2
'''
t = 10
for _ in range(1, t+1):
    tc = int(input())

    ans = 1
    # 100 * 100 배열
    arr = [list(input()) for _ in range(100)]
    # arr 배열의 전치행열
    n_arr = list(zip(*arr))

    for i in range(100):
        for j in range(100 - ans):
            # 회문 길이 최대 100, 가능한 길이를 모두 검사
            # ans 보다 큰 길이만 검사
            for p in range(ans, 100):
                # (i, j) 위치에서 길이 1 짜리 회문 만들기 => 가로, 세로
                # 회문의 길이가 배열 범위를 벗어나면 안됨.
                if j + p > 100:
                    break
                r = arr[i][j:j+p]
                c = n_arr[i][j:j+p]
                # 행이나 열의 값과 뒤집은 값이 같다면 ans 에 p 저장
                if r == r[::-1] or c == c[::-1]:
                    ans = p
    print(f'#{tc} {ans}')
'''
# 2001 파리 퇴치
'''
t = int(input())
for tc in range(1, t + 1):
    # n : 배열 길이, m : 파리채 길이
    n, m = map(int, input().split())
    # n * n 배열
    arr = [list(map(int, input().split())) for _ in range(n)]
    # 한번에 몇마리를 잡았는지 넣어줄 빈 리스트 생성
    flys = []
    for i in range(n-m+1):
        for j in range(n-m+1):
            # 파리 값 초기화
            fly = 0
            for p in range(m):
                for k in range(m):
                    fly += arr[i + p][j + k]
            # 리스트에 파리 수 넣어주기
            flys.append(fly)
    # 리스트에서 가장 큰 값 출력
    print(f'#{tc} {max(flys)}')
'''
# <재만 풀이>
# for tc in range(1, 1 + T):
#     # n x n 공간 , m x m 파리채
#     n, m = map(int, input().split())
#     box = [list(map(int, input().split())) for _ in range(n)]
#     max_cnt = -1
#     for i in range(n - m + 1):
#         for j in range(n - m + 1):
#             cnt = 0
#             for k in range(m):
#                 cnt += sum(box[i + k][j:j + m])
#             if max_cnt < cnt:
#                 max_cnt = cnt
#
#     print(f"#{tc} {max_cnt}")

# 파리퇴치 3
'''
t = int(input())
for tc in range(1, t + 1):
    # n : 배열 길이, m : 파리채 길이
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    # 한번에 몇마리를 잡았는지 넣어줄 빈 리스트 생성
    result = 0
    # 가로세로
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    for i in range(n):
        for j in range(n):
            sums = 0
            sums += arr[i][j]
            for p in range(4):
                for k in range(1, m):
                    r, c = i + dr[p] * k, j + dc[p] * k
                    if c < 0 or c >= n or r < 0 or r >= n:
                        break
                    sums += arr[r][c]
            if sums > result:
                result = sums
                sums = 0
    # 대각선
    dx = [-1, 1, 1, -1]
    dy = [1, 1, -1, -1]
    for i in range(n):
        for j in range(n):
            sums = 0
            sums += arr[i][j]
            for p in range(4):
                for k in range(1, m):
                    x, y = i + dx[p] * k, j + dy[p] * k
                    if x < 0 or x >= n or y < 0 or y >= n:
                        break
                    sums += arr[x][y]
            if sums > result:
                result = sums
    print(f'#{tc} {result}')
'''
# 9483 고대 유적
import sys
sys.stdin = open("input.txt", "r")
# 가장 긴 구조물의 길이
# 가로 세로 탐색 = 전치행렬
# 1이면 cnt += 1 max
t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    max_cnt = 0

    for r in range(n):
        cnt = 0
        for c in range(m):
            if arr[r][c] == 1:
                cnt += 1
                if cnt > max_cnt:
                    max_cnt = cnt
                else:
                    cnt = 0
    for c in range(m):
        cnt = 0
        for r in range(n):
            if arr[r][c] == 1:
                cnt += 1
                if cnt > max_cnt:
                    max_cnt = cnt
                else:
                    cnt = 0
    print(f'#{tc} {max_cnt}')


    # n_arr = list(zip(*arr))
    #
    # length = []
    # max_cnt = -1
    # for i in range(n):
    #     for j in range(m):
    #         cnt = 0
    #         if arr[i][j] == 1:
    #             cnt += 1
    #
    #         if cnt < max_cnt:
    #             max_cnt = cnt
    #             length.append(max_cnt)
    #             break

    print(max(length))
# # 4751. 다솔이의 다이아몬드 장식
# # D 5*5 # APPLE 5*21

# import sys
# sys.stdin = open("input.txt", "r")
#
# t = int(input())
# for tc in range(1, t+1):
#     n = input()
#     for _ in range(5):

