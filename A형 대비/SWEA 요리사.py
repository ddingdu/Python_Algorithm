import sys
sys.stdin = open('../input.txt', 'r')

def solve(num, alst, blst):
    global ans

    if num == n:
        if len(alst) == m:

            asum = bsum = 0
            for i in range(m):
                for j in range(m):
                    asum += arr[alst[i]][alst[j]]
                    bsum += arr[blst[i]][blst[j]]
            ans = min(ans, abs(asum - bsum))

        return

    solve(num+1, alst+[num], blst)
    solve(num+1, alst, blst+[num])

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    m = n // 2
    arr = [list(map(int, input().split())) for _ in range(n)]
    ans = 20000 * n * n
    solve(0, [], [])
    print(f'#{tc} {ans}')