'''
N = int(input())
for tc in range(1, N + 1):

    n = int(input())
    num_list = list(map(int, input().split()))

    ans_max = 0
    for i in range(n):
        if num_list[i] > ans_max:
            ans_max = num_list[i]

    ans_min = 999999999
    for x in range(n):
        if num_list[x] < ans_min:
            ans_min = num_list[x]

    print(f"#{tc} {ans_max-ans_min}")
'''
''' [ SWEA 1206 ]
n = int(input())

for tc in range(1, n + 1):

    N, M = map(int, input().split())

    num_ls = list(map(int, input().split()))

    ans = 0
    max_n = 0
    min_n = 9999999999

    # i : 시작 위치
    # i + j 가 구간합 위치
    for i in range(N - M + 1):  # 10 3 일때 8번
        for j in range(i, i + M):  # 1~3번째 인덱스 묶음 더하기

            ans = sum(num_ls[i:j + 1])

        if ans > max_n:
            max_n = ans
        if ans < min_n:
            min_n = ans

    print(f"#{tc} {max_n - min_n}")
'''


''' 제출 1
for tc in range(1, 11):

    N = int(input()) # 가로(건물 수)
    b_ls = list(map(int, input().split())) # 높이

    cnt = 0

    for i in range(2, N-2):
        b_max = max(b_ls[i-1],b_ls[i-2],b_ls[i+1],b_ls[i+2])
        if b_ls[i] > b_max:
            cnt += b_ls[i] - b_max

    print(f"#{tc} {cnt}")
'''
''' 제출 2 빌딩 조망권
import sys

sys.stdin = open("input_building.txt", "r")

for tc in range(1, 11):

    N = int(input()) # 가로(건물 수)
    b_ls = list(map(int, input().split())) # 높이

    cnt = 0

    # 앞 뒤 0 두 개 뺀 상태로 for문
    for i in range(2, N-2):
        # 왼쪽 2개, 오른쪽 2개 보다 크다면
        if b_ls[i] > b_ls[i-1] and b_ls[i] > b_ls[i-2] and b_ls[i] > b_ls[i+1] and b_ls[i] > b_ls[i+2]:
            # 양 옆 건물 중 높이가 가장 높은 값 만큼 빼주고 카운팅
            # 값 차이가 가장 적은 값이 높이가 가장 높기 때문에 반복문으로 두번째 높은 건물 찾기
            a1 = b_ls[i] - b_ls[i-2]
            a2 = b_ls[i] - b_ls[i-1]
            a3 = b_ls[i] - b_ls[i+1]
            a4 = b_ls[i] - b_ls[i+2]
            min_gap = a1
            for j in [a1,a2,a3,a4]:
                if j < min_gap:
                    min_gap = j
            cnt += min_gap


    print(f"#{tc} {cnt}")
'''
# #교수님 풀이
# import sys
#
# sys.stdin = open("input_building.txt", "r")
# T = 10
#
# for tc in range(1, T + 1):
#
#     n = int(input())
#
#     buildings = list(map(int, input().split()))
#
#     count = 0   # 답
#
#     # 앞부터 시작해서 끝까지 조망권 개수 구하기
#     for i in range(2, n - 2):  # 빌딩 양쪽 2칸은 비어있음 (높이가 0)
#         height = buildings[i]  # 현재 i 번째 위치 건물의 높이
#
#         # 현재 건물의 꼭대기부터 시작해서 조망권이 확보된 칸수 구하기
#         for floor in range(height, -1, -1):  # 위층부터 검사
# #             # 왼쪽, 오른쪽에 2칸씩 여유가 있는지 검사
#             if floor > buildings[i - 1] and floor > buildings[i - 2] and floor > buildings[i + 1] and floor > buildings[
#                 i + 2]:
#                 count += 1
#             else:
#                 # 조망권이 확보되지 않은 순간 밑층은 확인할 필요가 없으므로 반복 종료
#                 break
#
#     print(f"#{tc} {count}")




# 지혜님 풀이
'''
T = 10  # 테스트케이스 10개 고정
for tc in range(1, T + 1):

    # 윗칸에서부터 조망권의 갯수세기 (층 차이값의 합계)
    # 건물의 갯수 == 가로의 길이(전체구간)
    n = int(input())

    # 각 건물의 높이(층)
    h = list(map(int, input().split()))

    # 조망권이 있는 세대수의 합
    sum_total = 0

    # 전체 구간을 설정하기
    for i in range(2, n - 2):  # 1번째 5개, 2번째 5개...구간합 같이 범위가 반복된다

        # 두번째로 최대층 구하기
        max_floor = -1  # 초기값
        second_max_floor = -1

        for j in range(i - 2, i + 3):  # 5개 빌딩을 묶어서 양 옆 비교
            if h[i] - h[i - 2] >= 1 and h[i] - h[i - 1] >= 1 and h[i] - h[i + 1] >= 1 and h[i] - h[i + 2] >= 1:
                # 가운데건물을 기준으로 왼쪽 2개와 오른쪽 2개를 비교해서 각각 뺀 값이 1층 이상이면..
                # (동시충족조건으로 오른쪽에서도  1층 이상이어야 한다.)
                # 조망권확보의 조건인 양 옆 2칸이 충족되는 5개 배열임을 확인할 수 있다.

                # 5개 중에서 가장 큰 층(h[i])과 두번째로 큰 층의 차이가 조망권확보 세대수
                # 두번째 최대층 구하기
                if max_floor < h[j]:
                    second_max_floor = max_floor
                    max_floor = h[j]
                elif second_max_floor < h[j]:
                    second_max_floor = h[j]

        sum_total += (max_floor - second_max_floor)

    print(f"#{tc} {sum_total}")
'''
# 민 풀이
'''
    for tc in range(10):
         nn=int(input())
         a=list(map(int, input().split()))

         answer=[]
         zzinanswer=[]

         for i in range(2, len(a)-2):
            if a[i]>a[i-2] and a[i]>a[i-1] and a[i]>a[i+1] and a[i]>a[i+2]:
                answer.append(a[i-2:i+3])


         for x in answer:
            for j in range(len(x)-1):
                for i in range(len(x)-1):
                    if x[i] > x[i+1]:
                        x[i], x[i+1] = x[i+1], x[i]

         ssum=0
         for r in answer:
            ssum += (r[-1]-r[-2])
         print(f'#{tc+1} {ssum}')
'''

# 1970  거스름돈
'''
import sys
sys.stdin = open('input_money.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())    # 거스름돈
    # 리스트에 금액 별로 넣기
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    m_list = [0] * 8   # 화폐종류 8가지

    for i in range(len(money)):
        if N // money[i] != 0:
            m_list[i] = N // money[i]
            N = N % money[i]
    m_result = ' '.join(map(str, m_list))
    print(f'#{tc}\n{m_result}')

# 거스름돈 교수님 풀이
    # while N >= 50000:
    #     change[0] += 1
    #     n -= 50000
    # while N >= 10000:
    #     change[0] += 1
    #     n -+ 10000
    #
    # while N >= money[0]:
    #     change[0] += 1
    #     n -= money[0]
T = int(input())

for tc in range(1, T + 1):
    n = int(input())  # 거스름돈

    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
        # 화폐 종류 = 8가지
    change = [0] * 8
    # 화폐 종류 8가지에 대해 거스름돈 걸러주기 반복
    for i in range(8):
        cnt = 0
        # 남은 거스름돈 n 이 지금 화폐단위 money[i] 이상이라면 거스름돈으로 현재 화폐 사용 가능
        # 현재 화폐 가치만큼 거스름돈 빼주고 사용 횟수 증가
        while n >= money[i]:
            n -= money[i]
            cnt += 1
        # i 번째 화폐의 사용 갯수를 적어준다.
        change[i] = cnt

    print(f"#{tc}")

    ans = ""
    for c in change:
        ans += str(c) + " "
    print(ans)
'''


# SWEA 1966 - 버블정렬
# import sys
# sys.stdin = open('input_sort.txt','r')
#
#
# # 끝부터 범위를 하나씩 줄여가며 앞뒤로 스왑시킨다.스왑이 일어나지 않으면 정렬 완료.
#
#
# def sort_arr(N, arr):
#     for i in range(N-2, -1, -1):
#         swap = 0
#         for j in range(0, i+1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#                 swap = 1
#         if not swap:
#             return arr
#     return arr
#
# for ts in range(1, int(input())+1):
#     N = int(input())
#     a = list(map(int, input().split()))
#
#     for i in range(N - 1, 0, -1):  # 범위의 끝 위치
#         for j in range(0, i):
#             if a[j] > a[j + 1]:
#                 a[j], a[j + 1] = a[j + 1], a[j]
#
#     result_ls = ' '.join(map(str, a))
#
#     print(f'#{ts} {result_ls}')
# # 민풀이
#
# t = int(input())
# for tc in range(1, t + 1):
#     n = int(input())
#     a = list(map(int, input().split()))
#     for i in a:
#         for j in range(len(a) - 1):
#             if a[j] > a[j + 1]:
#                 a[j], a[j + 1] = a[j + 1], a[j]
#
#     a = ' '.join(map(str, a))
#     print(f'#{tc} {a}')



# 16192 전기버스
# import sys
#
# sys.stdin = open('input_bus.txt', 'r')

# T = int(input())

# for tc in range(1, T + 1):
#     cnt = 0
#     k, n, m = map(int, input().split())  # k:한번충전가동, n:종점, m:충전설치장소
#     chrg = list(map(int, input().split()))
#
#     rmn = k
#     point = 0
#     for i in range(len(chrg)):
#         if i == len(chrg) - 1:  # 마지막 위치
#             if n - point > rmn:
#                 cnt += 1
#
#         elif chrg[i] - point <= rmn:
#             if chrg[i + 1] - point > rmn:
#                 rmn = k
#                 cnt += 1
#             else:
#                 rmn -= (chrg[i] - point)
#             point = chrg[i]
#         else:  # 종점에 도착못할 경우
#             cnt = 0
#             break
#
#     print(f'#{tc} {cnt}')

# 전기 버스 교수님 풀이
# def drive(K, N):
#     # 버스를 운행하는 함수
#     # return == 0 : 충전소가 제대로 배치되어있지 않아서 완주 불가능
#     # return > 0 : 충전소가 제대로 배치되어 있다. ==> 충전 횟수를 리턴
#
#     last = 0 # 버스가 마지막으로 충전했던 위치
#     next = K # 버스가 최대로 이동한 위치 (초기값은 한번 이동한 상태로)
#     count = 0 # 충전한 횟수
#
#     # 버스가 종점에 도착할 때까지 계속 반복
#     while next < N:
#         # 버스가 이동한 위치에 충전기가 있나 없나 검사
#         while stop[next] == 0:
#             # 충전기가 없다면 뒤로 한칸 씩 돌아가면서 충전기를 찾을 때까지 뒤로 이동
#             next -= 1
#             if next == last:
#                 # 만약 뒤로 계속 가다가 내가 마지막으로 충전했던 위치까지 와버렸다면
#                 # 다시 앞으로 가봤자 다시 돌아올테니 충전소가 제대로 설치되지 않았다는 것!
#                 return 0    # 운행불가 ==> 함수가 바로 종료됨
#
#
#         # 충전기가 제대로 설치되어 있다면
#         # 마지막 충전 위치를 갱신
#         last = next
#         # 다음 위치로 이동
#         next += K
#         # 충전 횟수 1 증가
#         count +=  1
#         # 다음 위치로 이동했는데 이동한 거리가 N보다 크다면 완주했다는 의미, 반복 종료
#     return count
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     K, N, M = map(int,input().split())
#     # K = 한번 충전으로 이동할 수 있는 정류장 수
#     # N = 정류장 수
#     # M = 설치된 충전기 수
#     # 3, 10, 5 일때, 정류장 1,3,5,7,9 / 최소 충전횟수 = 3
#     charge = list(map(int,input().split()))
#     stop = [0] * N
#     for x in charge:
#         stop[x] = 1
#
#     answer = drive(K, N)
#
#     print(f"#{tc} {answer}")


# 16191 숫자카드

# import sys
#
# sys.stdin = open('input_card.txt', 'r')
#
# T = int(input())
#
# for tc in range(1, T + 1):
#
#     N = int(input())
#     number = input()
#
#     a = []
#     for i in str(number):
#         a.append(i)
#
#     num_ls = list(map(int, a))
#
#     result_ls = [0] * N
#     cnt = 0
#     for i in range(len(num_ls)-1):
#         for j in range(i-1):
#             if num_ls[i] == num_ls[j]:
#                 cnt += 1
#
#     # 교수님 풀이
#     counts = [0] * 10
#     # numbers 에 있는 숫자 하나씩 보면서 개수 세기
#     for num in number:
#         counts[int(num)] += 1 # num 카드의 등장 횟수 증가
#
#     # 카드의 최대 개수
#     max_count = 0
#     # 가장 큰 카드 수 (최대 개수 같은게 여러개 일 경우)
#     max_num = 0
#
#     for i in range(10):
#         if counts[i] >= max_count:
#             max_count = counts[i]
#             max_num = i
#     print(f"#{tc} {max_num} {max_count}")


# # 1208 box Flatten
# import sys
#
# sys.stdin = open('input_box flattern.txt.txt', 'r')
#
# for tc in range(1, 11):
#     n = int(input())
#     boxes = list(map(int, input().split()))
#
#     max_point = []
#     min_point = []
#
#     while n > 0:
#         max_point = [0, 0]
#         min_point = [0, 100]
#
#         for i in range(100):
#             if boxes[i] > max_point[1]:
#                 max_point = [i, boxes[i]]
#             if boxes[i] < min_point[1]:
#                 min_point = [i, boxes[i]]
#         boxes[max_point[0]] -= 1
#         boxes[min_point[0]] += 1
#
#         n -= 1
#
#     max_height = 0
#     min_height = 100
#
#     for i in range(100):
#         if boxes[i] > max_height:
#             max_height = boxes[i]
#         if boxes[i] < min_height:
#             min_height = boxes[i]
#
#     print(f'#{tc} {max_height-min_height}')
#
#
#
# #6485. 삼성시의 버스노선
# # for 문 돌려서 list에 append 해도됨
# import sys
#
# sys.stdin = open('0203 문제풀이 input.txt', 'r')
#
# # 첫 정류장 이상, 끝 정류장 이하 ???
#
# T = int(input())
#
# for tc in range(1, T+1):
#     N = int(input())    # 버스 노선 수:2
#
#     stops = [0] * 5001
#     # 각 노선 정보
#
#     for i in range(N):  # 각 노선 개수(n)만큼 반복
#         a, b = map(int, input().split())
#
#         for x in range(a, b+1):
#             stops[x] += 1
#
#     P = int(input())    # 정차 횟수 알고 싶은 정류장 수:5
#     stop_ls = []
#
#     for j in range(P):
#         C = int(input())
#         stop_ls.append(stops[C])
#
#     print(f'#{tc}', *stop_ls)

# 라이브 교수님 풀이

    # cnts = [0]*5001
    # for _ in range(N):
    #     S, E = map(int, input().split())
    #     for i in range(S, E+1):
    #         cnts[i]+=1
    #
    # P = int(input())
    # alst = []
    # for _ in range(P):
    #     p = int(input())
    #     alst.append(cnts[p])
    # a = ' '.join(map(str, alst))
    #
    # print(f'#{tc} {a}')


# 13616 1945 간단한 소인수분해 (라이브 교수님풀이)
#
# divs = [2,3,5,7,11]
#
# T = int(input())
#
# for tc in range(1, T + 1):
#     N = int(input())
#     cnts = [0]*len(divs)
#
#     for i in range(len(divs)):
#         while N % divs[i] == 0:
#             cnts[i] += 1
#             N = N//divs[i]
#
#     print(f'#{tc}', *cnts)

# 9386  연속한 1의 수 (라이브 교수님풀이)
# T = int(input())
#
# for tc in range(1, T + 1):
#     N = int(input())
#     lst = list(map(int, input()))
#     ans = 0
#     cnt = 0
#     for i in range(N):
#         if lst[i] == 0:
#             cnt = 0
#         else:
#             cnt += 1
#             if ans < cnt:
#                 ans = cnt
#
#     print(f'#{tc}', ans)

#6019 기차 사이의 파리
# T = int(input())
#
# for tc in range(1, T + 1):
#     D, A, B, F = map(int, input().split())
#     ans = D / (A + B) * F
#
#     print(f'#{tc} {ans}')

# # 9367 점점 커지는 당근의 개수
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    x = list(map(int, input().split()))

    max_num = 0

    for i in range(N-1):
        cnt = 1
        if x[i] + 1 == x[i+1]:
            cnt += 1

        elif x[i] != x[i+1]:
            max_num = cnt
            cnt = 0

    if max_num < cnt:
        cnt = max_num

    print(f'#{tc} {cnt}')
#####
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    x = list(map(int, input().split()))
    cnt = 1
    max_cnt = 0
    max_v = x[0]

    for i in range(1, len(x)):
        if x[i] > max_v:
            cnt += 1
            max_v = x[i]
        else:
            max_v = x[i]
            cnt = 1
        if max_cnt < cnt:
            max_cnt = cnt

    print(f'#{tc} {cnt+1}')
# 재만풀이
T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    n_list = list(map(int, input().split()))
    cnt = 1
    max_cnt = -1
    max_v = n_list[0]

    for i in range(1, len(n_list)):
        if n_list[i] > max_v:
            cnt += 1
            max_v = n_list[i]
        else:
            max_v = n_list[i]
            cnt = 1

        if max_cnt < cnt:
            max_cnt = cnt

    print(f"#{tc} {max_cnt}")

# 13994 새로운 버스 노선

# 일반 : 모두 정차
# 급행 : A가 짝수인 경우 짝수 / A가 홀수인 경우 홀수
# 광역급행 : A가 짝수인 경우 4배수 / A가 홀 수인 경우 3배수 AND 10배수X
# => 최대 몇 개 노선이 같은 정류장에 정차?
# T = int(input())
#
# for tc in range(1, T + 1):
#     n = int(input())  # 노선의 수
#
#     bus_list = [list(map(int, input().split())) for _ in range(n)]  # 버스 정보
#     print(bus_list)
#     stop_cnt = [0] * 1001  # 정류장에 정차하는 버스의 개수 최대값 구하기
#     # stop_cnt[i] => i번 정류장에 정차하는 버스의 수
#
#     # 버스 노선 수만큼 반복
#     for bus in bus_list:
#         '''
#         1. 일반버스 : 모든 정류장에 정차
#         2. 급행버스
#             2-1. 시작 정류장이 짝수 : 짝수 번호 정류장에만 정차
#             2-2. 시작 정류장이 홀수 : 홀수 번호 정류장에만 정차
#         3. 광역급행버스
#             3-1. 시작 정류장이 짝수 : 4의 배수 번호 정류장에만 정차
#             3-2. 시작 정류장이 홀수 : 3의 배수 번호 정류장이면서 10의 배수가 아닌 정류장에만 정차
#         '''
#         # 시작, 끝 정류장은 반드시 정차
#         stop_cnt[bus[1]] += 1
#         stop_cnt[bus[2]] += 1
#
#         # 버스의 시작점 + 1 부터 시작해서 종료점 -1 까지 조건 확인
#         for i in range(bus[1] + 1, bus[2]):
#             # 일반 버스
#             if bus[0] == 1:
#                 stop_cnt[i] += 1
#             # 급행 버스
#             elif bus[0] == 2:
#                 # 2-1. 짝수
#                 if bus[1] % 2 == 0 and i % 2 == 0:
#                     stop_cnt[i] += 1
#                 # 2-2. 홀수
#                 if bus[1] % 2 == 1 and i % 2 == 1:
#                     stop_cnt[i] += 1
#             # 광역 급행 버스
#             else:
#                 # 3-1. 짝수
#                 if bus[1] % 2 == 0 and i % 4 == 0:
#                     stop_cnt[i] += 1
#                 # 3-2. 홀수
#                 if bus[1] % 2 == 1 and i % 3 == 0 and i % 10 != 0:
#                     stop_cnt[i] += 1
#     # 최대값 구하기
#     answer = 0
#     for cnt in stop_cnt:
#         if answer < cnt:
#             answer = cnt
#     print(f"#{tc} {answer}")
#

#