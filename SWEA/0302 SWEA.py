import sys
sys.stdin = open('../23.03.29_분할정복/input.txt', 'r')

'''
#1 11
#2 44
'''
# 러시아 국기 같은 깃발
'''
# N행 M열 / 최소 1줄 이상 흰.파.빨 W B R
# 새로 칠해야 하는 칸의 개수의 최솟값

# 4: 1/1/2 1/2/1 2/1/1
# 6 1/1/4 1/2/3 1/3/2 1/4/1 2/2/2 2/1/3 2/3/1 ... 

# 많으면 많은 색으로 바꾸기?
# 해당 색 아니면 cnt += 1
# 해당 색이면 cnt += 1 하고 m 에서 빼기?


t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr = [list(input()) for _ in range(n)]
    cnt = 0

    for j in range(m):
        # 첫줄 W 아니면 세고 W 로 바꾸기
        if arr[0][j] != 'W':
            cnt += 1
            arr[0][j] = 'W'
        # 마지막 줄 R 아니면 세고 R 로 바꾸기
        if arr[-1][j] != 'R':
            cnt += 1
            arr[-1][j] = 'R'

    #     W = B = R = 0
    # for j in range(m):
    #     if arr[1][j] == 'W':
    #         W += 1
    #     if arr[1][j] == 'B':
    #         B += 1
    # 
    #     if W > B:
    #         arr[1][j] = 'W'
    #         cnt += m - W
    #     else:
    #         arr[1][j] = 'B'
    #         cnt += B
    # 
    # for j in range(m):
    #     if arr[-2][j] == 'R':
    #         R += 1
    #     if arr[-2][j] == 'B':
    #         B += 1
    # 
    #     if R > B:
    #         arr[1][j] = 'R'
    #         cnt += m - R
    #     else:
    #         arr[1][j] = 'B'
    #         cnt += B
    # 
    # print(W, B, R)

    print(arr)
    blue = 0
    # 전체 배열에서 B 이면 세기
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 'B':
                blue += 1
    # 첫줄 끝줄 뺀 전체에서 B 개수 뺀 값 cnt 에 더하기
    cnt += (n-2) * m - blue

    print(cnt)

'''
# 달란트 2
'''
# 달란트를 묶음 수로 나눠서 곱한 값의 최대
# 어떻게 나눠야 가장 큰 수가 나올지?
t = int(input())
for tc in range(1, t+1):
    # n: 달란트 개수, p: 묶음 수
    n, p = map(int, input().split())

    # 나머지가 없는 경우
    if n % p == 0:
        a = b = n // p
        ans = a ** p

    # 나머지가 있다면 c 에 저장
    else:
        c = n % p
        a = n // p
        b = n // p + c

        # 묶음 수에서 c(나머지)를 뺀 값을 제곱하고
        # 남은 묶음 수에 c(나머지)를 분배해서 c 제곱
        ans = (a ** (p-c)) * ((a + c//c) ** c)

    print(f'#{tc} {ans}')
'''
'''
풀이시간 3-40분
처음에 테케 3개(1, 2, 7)만 맞음
홀짝 나눠서 경우의 수 생각하기
변수명 고민하기
각주 설명 보완하기
'''

# 원재의 메모리 복구하기
'''
t = int(input())
for tc in range(1, t+1):
    memory = list(input())
    # 초기값 ([0]리스트)
    zero = ['0'] * len(memory)
    cnt = 0

    for i in range(len(memory)):
        # 메모리와 [0]리스트의 i 인덱스가 다른 값이라면 +1
        if memory[i] != zero[i]:
            cnt += 1
            # 값이 다른 위치(i)부터 메모리 끝까지 다시 탐색
            for j in range(i, len(memory)):
                # 값이 다른 위치부터 [0]리스트와 똑같은 인덱스 번호 자리에 메모리 값 쭉 저장
                zero[j] = memory[i]
            # 메모리와 [0]리스트가 같아지면 반복문 종료, 같지 않다면 다시 반복
            if memory == zero:
                break

    print(f'#{tc} {cnt}')
'''

# 현주의 상자 바꾸기
'''
# 처음에는 상자 숫자 모두 0
# i 번째 작업에 대해 l번 상자부터 r번 상자까지 값을 i로 변경

t = int(input())
for tc in range(1, t+1):
    # n: 상자 개수, q: 작업 횟수
    n, q = map(int, input().split())
    # 인덱스 번호 맞춰주기 위해 (n+1) 만큼 만들어주기
    box = [0] * (n+1)

    for i in range(1, q+1):
        # l: l번 상자부터 , r: r번 상자까지
        l, r = map(int, input().split())
        for p in range(l, r + 1):
            box[p] = i

    print(f'#{tc}', *box[1:])
'''
''' Review
30분 이내
리스트의 인덱스 번호 0부터 시작하므로 1부터 시작, +1 까지로 범위 설정 
결과 값 출력할 때 리스트 벗기고 숫자만 꺼낼 때 *사용
join 함수는 문자열 리스트 일 때 사용 가능
'''

'''
7 33 44
3471 6365 10306 4658 1 9400 2371

#9 Impossible
'''
# 진기의 최고급 붕어빵
# 30번 불가능
# m초 동안 k개 만들 수 있음

# 안될 경우
# 시작 손님 굽는 시간도 전에 오면 바로 불가능

t = int(input())
for tc in range(1, t+1):
    # n: 사람 수, m: 시간(초), k: 붕어빵 개수
    n, m, k = map(int, input().split())
    # 시간 n개
    time_lst = list(map(int, input().split()))
    mx_time = max(time_lst)
    mn_time = min(time_lst)
    fish = m * k
    ans = 'Possible'

    if mx_time < m:
        ans = 'Impossible'

    if time_lst[0] < m:
        ans = 'Impossible'
    if mn_time < m:
        ans = 'Impossible'

    for i in range(len(time_lst)):
        idx_num = i + 1

    print(f'#{tc} {ans}')






















