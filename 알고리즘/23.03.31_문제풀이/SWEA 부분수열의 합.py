import sys
sys.stdin = open('../input.txt', 'r')

def dfs(n, sm):
    global cnt

    # 가지 치기
    if sm > K:
        return
    # 종료 조건
    if n == N:
        if sm == K:
            cnt += 1
        return

    dfs(n+1, sm + lst[n])
    dfs(n+1, sm)

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    lst = list(map(int, input().split()))
    cnt = 0
    dfs(0, 0)
    print(f'#{tc} {cnt}')