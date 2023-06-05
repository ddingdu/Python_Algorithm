import sys
sys.stdin = open('input.txt', 'r')

def dfs(n, sm, now):
    global cnt

    if n == A:
        if sm == K and now == N:
            cnt += 1
        return

    dfs(n+1, sm+lst[n], now+1)
    dfs(n+1, sm, now)

T = int(input())
for tc in range(1, T + 1):
    # N:원소 개수, K:원소 합
    N, K = map(int, input().split())
    lst = list(range(1, 13))
    A = 12
    cnt = 0
    dfs(0, 0, 0)
    print(f'#{tc} {cnt}')