# import sys
#
# sys.stdin = open("input.txt", "r")
#
# T = int(input())
#
# for tc in range(1, T+1):
#     # 가로 칸의 수
#     n = int(input())
#     # 상자 탑 높이 정보
#     box = int(input())
#     # 최댓값 => 초기값 정할 때 적당히 작은 값
#     # 최솟값 => 적당히 큰 값
#     ans = 0
#
#     # 반복문을 돌면서 현재 위치의 높이에서 제일 위에
#     # 있는 상자의 낙차 중에 가장 큰 값 구하기
#
#         # 현재 위치에서 맨 꼭대기 상자가 오른쪽에 장애물 없다고 했을 때 최대 낙차 구하기
#
#         # print(height)
#         # 또 반복문을 돌면서 현재 '내 위치 기준', 오른쪽에 있는 장애물 수 구하기
#
#             # 내 위치 (i) 기준 오른쪽 : i + 1
#             # 현 위치 상자 높이 : box[i]
#             # 현 위치 기준 오른쪽 상자 높이 : box[j]
#
#
#     # 최대 낙차 = 현재 위치에서 오른쪽에 상자가 없을 경우 최대 낙차 - 오른쪽 상자수
#
#     # 최대 낙차 중 최댓값을 갱신
#     print(f"#{tc} {ans}")


# n = 50005
# idx = [0] * 5
#
# # a = 10
# # b = 50
#
# if n >= 50000:
#     idx[0] = n // 50000
#     if n % 50000 >= 10000:
#         idx[1] = n // 10000
#         if n % 10000 > = 5000;
#         idx[2] = n // 5000

# T = int(input())
#
# for tc in range(1, T + 1):
#     n = int(input())  # 노선의 수
#
#     bus_list = [list(map(int, input().split())) for _ in range(n)]  # 버스 정보
#     print(bus_list)

# t = int(input())
#
# for tc in range(1, t + 1):
#     n = int(input())
#     nums = list(map(int, input().split()))
#     ls = [0] * n
#
#     for i in range(n - 1):
#         min_idx = i
#         for j in range(i + 1, n):
#             if nums[min_idx] > nums[j]:
#                 min_idx = j
#
#         if i % 2 == 0:
#             ls[i] = nums[min_idx]
#     print(ls)




# def selection_sort(arr, n):
#
#     for i in range(n - 1):
#         min_idx = i
#         # i 의 뒤부터 비교를 시작하면서 최솟값을 찾는다.
#         for j in range(i + 1, n):
#             # 제일 작은 숫자의 인덱스 찾기
#             if arr[min_idx] > arr[j]:
#                 min_idx = j
#
#         arr[i], arr[min_idx] = arr[min_idx], arr[i]
#
#         return
#
# arr = [10, 30, 40, 50]
# n = len(arr)
# selection_sort(arr, n)

# arr = [10, 70, 40, 30, 50]
# n = len(arr)
#
# for i in range(n - 1):
#     min_idx = i
#     # i 의 뒤부터 비교를 시작하면서 최솟값을 찾는다.
#     for j in range(i + 1, n):
#         # 제일 작은 숫자의 인덱스 찾기
#         if arr[min_idx] > arr[j]:
#             min_idx = j
#
#     arr[i], arr[min_idx] = arr[min_idx], arr[i]
# print(arr)

# num_dict = {'ZRO': 0, 'ONE': 1, 'TWO': 2, 'THR': 3, 'FOR': 4, 'FIV': 5, 'SIX': 6, 'SVN': 7, 'EGT': 8, 'NIN': 9}
# print(num_dict.values())

# def prime(n):
#     primes = []
#     for i in range(2, n+1):
#         # i를 기준으로 해서 i를 j로 나눴을 때 나머지가 0이면 배수 ==> 체크
#         # j의 범위는 2 <= j < i
#         for j in range(2, i):
#             if i % j == 0:
#                 break
#         else:
#             primes.append(i)
#     return primes
# print(prime(7))

# n = 1000    # 2부터 1000까지의 모든 수에 대하여 소수 판별
# is_prime = [True for i in range(n + 1)] # 처음엔 모든 수가 소수인 것으로 초기화
# for i in range(2, int(n ** 0.5) + 1):
#     if is_prime[i]: # i가 소수인 경우
#         # i를 제외한 모든 i의 배수를 지우면 된다 (False)로 체크
#         j = 2
#     while i * j <= n:
#         is_prime[i * j] = False
#         j += 1
# print(is_prime.count(True)-2)   # 0, 1 제외한 소수 개수
#
# a = [0, 13, 15]
# b = str(a)
# print(b)
# if str(3) in b:
#     cnt = 1
# print(cnt)

# n = 3
# a = 1 2 3
# arr = [ a * n for _ in range(n)]
# arr_t = list(map(list, zip(*arr)))
# print(arr_t)
# print(*arr)





# 연습문제 3
'''
7 8
1 2
1 3
2 4
2 5
4 6
5 6
6 7
3 7
'''

# def dfs(s, V):
#     visited = [0] * (V + 1)
#     stack = []
#
#     i = s
#     visited[i] = 1
#
#     while True:
#         for w in range(1, V+1):
#             if adj[i][w] == 1 and visited[w] == 0:
#                 stack.append(i)
#                 i = w
#                 visited[w] = 1
#                 break
#         else:
#             if stack:
#                 i = stack.pop()
#             else:
#                 break
#     return
# #       0  1  2  3  4  5  6  7
# adj = [[0, 0, 0, 0, 0, 0, 0, 0], # 0
#        [0, 0, 1, 1, 0, 0, 0, 0], # 1
#        [0, 1, 0, 0, 1, 1, 0, 0], # 2
#        [0, 1, 0, 0, 0, 0, 0, 1], # 3
#        [0, 0, 1, 0, 0, 0, 1, 0], # 4
#        [0, 0, 1, 0, 0, 0, 1, 0], # 5
#        [0, 0, 0, 0, 1, 1, 0, 1], # 6
#        [0, 0, 0, 1, 0, 0, 1, 0]] # 7
#
# node = ["", 1, 2, 3, 4, 5, 6, 7]
#
# V, E = map(int, input().split())
# adj = [[0] * (V + 1) for _ in range(V + 1)]
# for i in range(E):
#     start, to = map(int, input().split())
#     adj[start][to] = 1
#     # 무향 그래프 (방향이 없는 그래프)만 아래 추가
#     adj[to][start] = 1
#
# print(dfs(1, 7))
# 1 2 4 6 5 7 3



def dfs(s, V):
    visited = [0] * (V+1)
    stack = []
    # i: 현위치 정점
    i = s   # 현위치 정점에서 시작
    visited[i] = 1

    while True:
        # w: v와 이어진 다음 정점
        for w in range(1, V+1):
            #  w 로 가는 길 있고(adj[i][w]=1), w 방문한 적 없다면(visited[w]=0)
            if adj[i][w] == 1 and visited[w] == 0:
                # 현위치 i 를 스택에 저장 (w 로 가는 길 있기 때문)
                stack.append(i)
                i = w   # 현위치 정점을 다음 정점 w 로 변경
                visited[w] = 1  # w 에 방문했다는 뜻
                break   # 다른 방향으로 가지 않도록 탐색 종료
        # 현위치 i에서 탐색 해봣는데 갈 수 있는 정점 없다면
        else:
            # 최근 방문했던 정점(스택에서 pop) 찾아서 그 위치로 돌아감
            if stack:   # 스택에 값이 있다면 pop
                i = stack.pop()
            else:   # 스택에 값이 없다면 탐색 종료
                break
    return
# 인접 행렬
#       x  A  B  C  D  E  F  G
adj = [[0, 0, 0, 0, 0, 0, 0, 0],  # X
       [0, 0, 1, 1, 0, 0, 0, 0],  # A
       [0, 1, 0, 0, 1, 1, 0, 0],  # B
       [0, 1, 0, 0, 0, 1, 0, 0],  # C
       [0, 0, 1, 0, 0, 0, 1, 0],  # D
       [0, 0, 1, 1, 0, 0, 1, 0],  # E
       [0, 0, 0, 0, 1, 1, 0, 1],  # F
       [0, 0, 0, 0, 0, 0, 1, 0]]  # G

node = ["", "A", "B", "C", "D", "E", "F", "G"]
V, E = map(int, input().split())
adj = [[0] * (V+1) for _ in range(V+1)]
for i in range(E):
    start, end = map(int, input().split())
    adj[start][end] = 1
    # 양방향 가능하므로 전치해서 추가
    adj[end][start] = 1

dfs(1, 7)



