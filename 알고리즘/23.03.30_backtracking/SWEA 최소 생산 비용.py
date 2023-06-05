import sys
sys.stdin = open('../input.txt', 'r')


def backtrack(i):
    global sum, ans

    if ans <= sum:    # 가지치기
        return

    if i == N:    # 종료 조건
        if sum < ans:
            ans = sum
        return

    for j in range(N):
        if v[j] == 0:
            v[j] = 1
            sum += arr[i][j]
            backtrack(i + 1)
            # 재귀가 종료되면, 재귀 호출 전 원위치로 돌아가기
            v[j] = 0
            sum -= arr[i][j]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    v = [0] * N
    sum = 0
    ans = 10000

    backtrack(0)
    print(f'#{tc} {ans}')
