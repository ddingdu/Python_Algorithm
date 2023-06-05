'''
중복 수열 x
부분 수열
'''
def dfs(n, lst):
    # 종료 조건
    if n == M:
        ans.append(lst)
        return

    # dfs(n + 1, lst)
    for i in range(1, N+1):
        dfs(n+1, lst+[i])

N, M = map(int, input().split())
ans = []
dfs(0, [])

for lst in ans:
    print(*lst)