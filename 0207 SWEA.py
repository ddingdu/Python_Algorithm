# swea 1954 달팽이 숫자

# 배열 범위를 벗어나거나 이미 숫자 있으면 꺾어야함
# 값이 다 0인 2차원 배열 만들기 (자리 주인 정해지지 않았다)
'''
t = int(input())
# 방향 : 우-하-좌-상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

for tc in range(1, t+1):
    n = int(input())
    arr = [[0]*n for _ in range(n)]

    # 현재 위치 0, 0 부터 시작
    r, c = 0, 0
    # d를 1씩 증가시켜주면 방향을 바꾸는 것??????
    d = 0
    # 1 부터 n*n까지 반복
    for i in range(1, n * n + 1):
        # i 는 달팽이 안에 들어갈 숫자, 1부터 증가
        # 현 위치에 1부터 i를 차례대로 넣기
        arr[r][c] = i

        # 다음 위치 계산
        next_row = r + dr[d]
        next_col = c + dc[d]

        # 다음 위치가 유효한 인덱스?? 배열 범위를 벗어나지 않았고, 다음 위치에 있는 숫자가 0
        if 0 <= next_row < n and 0 <= next_col < n and arr[next_row][next_col] == 0:
            # ==> 현 위치를 다음 위치로 변경
            r, c = next_row, next_col
        # 다음 위치가 유효하지 않다면??
        # ==> 방향을 바꾸고 다음 위치 계산 후 현재 위치를 다음 위치로 변경
        else:
            # d += 1
            # if d == 4:
            #     d = 0
            d = (d + 1) % 4
            r = r + dr[d]
            c = c + dc[d]
    print(f'#{tc}')
    # for nums in arr:
    #     print(*nums)
    for i in range(n):
        print(*arr[i])
'''
#  특별한 정렬 (교수님 풀이)
'''
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    nums = list(map(int, input().split()))

    # 바꿀 대상 위치 (최대값 or 최소값)
    index = 0

    for ni in range(10):
        for j in range(ni, n):
            if ni % 2 == 0 and nums[j] > nums[index]:
                # 최대값 인덱스
                index = j
            if ni % 2 == 1 and nums[j] < nums[index]:
                # 최소값 인덱스
                index = j

        nums[ni], nums[index] = nums[index], nums[ni]

    print(f"#{tc}", " ".join(map(str, nums[:10])))
# 구글 풀이
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    # 특별히 정렬된 숫자를 10개까지만 출력
    for i in range(0, 10, 2):
        # 큰 값 구해서 맨 앞으로
        max_v = i
        for j in range(i+1, N):
            if arr[max_v] < arr[j]:
                max_v = j
        arr[i], arr[max_v] = arr[max_v], arr[i]

        # 작은 값 구해서 큰 값 바로 뒤
        min_v = i+1
        for k in range(i+2, N):
            if arr[min_v] > arr[k]:
                min_v = k
        arr[i+1], arr[min_v] = arr[min_v], arr[i+1]

    print(f'#{tc}', *arr[0:10])
'''
# 이진탐색(교수님 풀이)
'''
T = int(input())
for tc in range(1, T+1):
    # p:페이지수/a: /b:찾아야할 페이지
    p, a, b = map(int, input().split())

    winner = ""

    a_start, a_end = 1, p
    b_start, b_end = 1, p

    # 페이지를 찾을 때까지 반복 진행
    while True:
        a_find = False # a가 페이지를 찾았는지
        b_find = False # b가 페이지를 찾았는지

        # a 부터 페이지를 찾기 시작
        mid = (a_start + a_end) // 2
        if mid == a:
            a_find = True
        elif mid > a:
            a_end = mid
        else:
            a_start = mid
        # b도 페이지를 찾기
        mid = (b_start + b_end) // 2
        if mid == b:
            b_find = True
        elif mid > b:
            b_end = mid
        else:
            b_start = mid

        if a_find and b_find:
            winner = 0
            break
        if a_find:
            winner = "A"
            break
        if b_find:
            winner = "B"
            break

    print(f'#{tc} {winner}')
'''
# Sum
# 승현 풀이
for test_case in range(1, 11):

    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(100)]

    max_V = sum_1 = sum_2 = 0
    for i in range(100):
        sum_1 += arr[i][i]
        sum_2 += arr[i][99 - i]
        sum_r = sum_h = 0
        for j in range(100):
            sum_r += arr[i][j]
            sum_h += arr[j][i]

        max_V = max(max_V, sum_r, sum_h)

    max_V = max(max_V, sum_1, sum_2)

    print(f'#{test_case} {max_V}')


# Ladder

# T = 10
# for tc in range(1, T+1):
#     nums = list(map(int, input().split()))
#     # 100*100 배열
#     ladder = [[0]*100 for _ in range(100)]

T = 10
for tc in range(1, T + 1):
    # N : 테스트 케이스의 번호
    N = int(input())
    # arr : 1-사다리, 0-여백, 2-도착지점
    arr = [list(map(int, input().split())) for _ in range(100)]

    # 도착지점에서 거꾸로 찾아가기

    # 도착지점 2가 어디에 있는지 idx 찾기
    # end : 사다리 결과 도착지점, 거꾸러 찾아가는 길의 시작지점
    end_r = 99
    end_c = 0
    for j in range(100):
        if arr[99][j] == 2:
            end_c = j

    # 오른쪽 or 왼쪽에 1 있을 경우 따라서 이동
    # 없으면 위로 이동

    # 위에 아무것도 없다면(arr[0][]) 이면 멈춰서 그 자리의 열의 위치 말하기
    while end_r != 0:
        # 오른쪽이 1이면 오른쪽에 0이 나올때까지 이동 + 위로 한 칸 이동
        if 0 <= end_c + 1 <= 99 and arr[end_r][end_c + 1]:
            while end_c + 1 <= 99 and arr[end_r][end_c + 1]:
                end_c += 1
            end_r -= 1
        # 왼쪽이 1이면 왼쪽에 0이 나올때까지 이동 + 위로 한 칸 이동
        elif 0 <= end_c - 1 <= 99 and arr[end_r][end_c - 1]:
            while 0 <= end_c - 1 and arr[end_r][end_c - 1]:
                end_c -= 1
            end_r -= 1
        # 옆에 1이면 위로 이동
        else:
            end_r -= 1

    # print(f & apos;  # {N} {end_c}&apos;)
    print(f'#{tc} {end_c}')

