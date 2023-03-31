import sys
sys.stdin = open('../input.txt', 'r')

def dfs(n, sm):
    global ans

    if n == N:
        if sm >= B:
            ans = min(ans, sm-B)
        return

    dfs(n+1, sm+lst[n])
    dfs(n+1, sm)

T = int(input())
for tc in range(1, T + 1):
    N, B = map(int, input().split())
    lst = list(map(int, input().split()))
    ans = N * 10000    # 10000:점원 키의 최대
    dfs(0, 0)
    print(f'#{tc} {ans}')