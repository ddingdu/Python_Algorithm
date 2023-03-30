

def dfs(n, lst):

    if n == M:

        return


N, M = map(int, input().split())
ans = []
dfs(0, [])

for lst in ans:
    print(*lst)