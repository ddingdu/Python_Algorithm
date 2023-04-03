# 문제 1: 정원에 나무심기

# 가장 왼쪽 세로 줄부터 나무 심기, 한 줄 씩 띄어서 심기(홀수 열)
# 가장 비싼 나무 가격과 해당 나무의 열 번호 계산 (가격 같을 경우 가장 큰 열 번호로)
# 총 비용/심은 나무 수/가장 비싼 가격/심어진 열
# cost/tree/mx_cost/ans
import sys
sys.stdin = open('../input.txt', 'r')

t = int(input())
for tc in range(1, t+1):
    # n: 행 개수, m: 열 개수
    n, m = map(int, input().split())
    # n 행 배열
    arr = [list(map(int, input().split())) for _ in range(n)]

    cost = []    # 나무 비용 담을 리스트
    j_lst = []    # 열 번호 담을 리스트

    # 홀수 열만 탐색하기 위해 2칸씩 건너서 보기
    for j in range(0, m+1, 2):
        for i in range(n):
            if 0 <= j < m and 0 <= i < n:
                # 홀수 열에 있는 비용만 리스트에 넣어주기
                cost.append(arr[i][j])
                # 열 번호(j) 만 넣어주기
                j_lst.append(j)

    mx_cost = 0
    # 가장 비싼 비용이랑 같은 인덱스의 열 번호(j) 구하기
    for c in range(len(cost)):
        if cost[c] > mx_cost:
            mx_cost = cost[c]

    result = 0
    # 가장 비싼 비용의 인덱스 구하기
    for idx in range(len(cost)):
        # 비용 리스트 값이 가장 비싼 비용과 같다면 result 에 인덱스 번호 저장
        if cost[idx] == mx_cost:
            result = idx

    # 0 열 부터 시작했으므로 + 1 해서 결과 값 출력
    ans = j_lst[result] + 1

    # 총 비용 / 심은 나무 수 / 가장 비싼 나무 가격 / 가장 비싼 나무가 심어진 열
    print(f'#{tc} {sum(cost)} {len(cost)} {mx_cost} {ans}')

# 문제 2: 별

# 별자리가 빠짐없이 나오면서 최대 크기로 별자리 사진을 찍기 위해 몇 번 확대해야 하는지 ???
# 확대 시 별자리 비율은 커지지만 촬영 영역은 작아진다
# 최대 확대 횟수 출력
# 주어진 조건에서 모든 별 촬영할 수 없을 경우 : -1


t = int(input())
for tc in range(1, t+1):
    # n: 하늘 크기, k: 촬영 영역, a, b: 초점 좌표
    n, k, a, b = map(int, input().split())
    # 전체 하늘 n * n 배열
    arr = [input().split() for _ in range(n)]

    ans = -1

    star = 0
    # 배열 내 별의 총 개수 세기
    for lst in arr:
        star += lst.count('*')

    # k * k 는 a, b 좌표로부터 + k//2 씩 범위
    e1, e2 = a + k//2, b + k//2
    s1, s2 = a - k//2, b - k//2

    cnt = 0
    for i in range(s1, e1+1):
        for j in range(s2, e2+1):
            if 0 <= i < k and 0 <= j < k:
                if arr[i][j] == '*':
                    cnt += 1
    if star == cnt:
        ans = 0

    cnt = 0
    for i in range(s1+1, e1):
        for j in range(s2+1, e2):
            if 0 <= i < k and 0 <= j < k:
                if arr[i][j] == '*':
                    cnt += 1
    if star == cnt:
        ans = 1

    cnt = 0
    for i in range(s1+2, e1-1):
        for j in range(s2+2, e2-1):
            if 0 <= i < k and 0 <= j < k:
                if arr[i][j] == '*':
                    cnt += 1
    if star == cnt:
        ans = 2

    cnt = 0
    for i in range(s1+3, e1-2):
        for j in range(s2+3, e2-2):
            if 0 <= i < k and 0 <= j < k:
                if arr[i][j] == '*':
                    cnt += 1
    if star == cnt:
        ans = 3

    cnt = 0
    for i in range(s1+4, e1-3):
        for j in range(s2+4, e2-3):
            if 0 <= i < k and 0 <= j < k:
                if arr[i][j] == '*':
                    cnt += 1
    if star == cnt:
        ans = 4

    cnt = 0
    for i in range(s1 + 5, e1 - 4):
        for j in range(s2 + 5, e2 - 4):
            if 0 <= i < k and 0 <= j < k:
                if arr[i][j] == '*':
                    cnt += 1
    if star == cnt:
        ans = 5

    cnt = 0
    for i in range(s1+6, e1-5):
        for j in range(s2+6, e2-5):
            if 0 <= i < k and 0 <= j < k:
                if arr[i][j] == '*':
                    cnt += 1
    if star == cnt:
        ans = 6

    print(f'#{tc} {ans}')


