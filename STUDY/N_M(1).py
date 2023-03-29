'''
중복 X
'''

# def dfs(n, lst):
#     if n == M:
#         ans.append(lst)
#         return
#
#     for i in range(1, N+1):
#         if v[i] == 0:
#             v[i] = 1
#             dfs(n+1, lst+[i])
#             v[i] = 0
#
# N, M = map(int, input().split())
# ans = []
# v = [0] * (N+1)
# dfs(0, [])
#
# for lst in ans:
#     print(*lst)


'''
같은 수 여러번 가능
중복 수열 X
'''
# def dfs(n, lst):
#     if n == M:
#         ans.append(lst)
#         return
#
#     for i in range(1, N+1):
#         dfs(n+1, lst+[i])
#
# N, M = map(int, input().split())
# ans = []
# dfs(0, [])
#
# for lst in ans:
#     print(*lst)


'''
조합 n개중에 r개 뽑기 nCr
순열 P
'''
def dfs(n, s, lst):
    if n == M:
        ans.append(lst)
        return

    for i in range(1, N+1):
        dfs(n+1, lst+[i])

N, M = map(int, input().split())
ans = []
dfs(0, 1, [])

for lst in ans:
    print(*lst)
