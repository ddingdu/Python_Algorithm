
# i:행번호/lst:담당이 지정된 일들의 열 값/total:현재까지 확률
def dfs(i, lst, total):
    global ans
    # 가지치기
    if total <= ans:
        return
    # 종료 조건:
    if i == N:    # 모든 일의 담당자 배정 됨
        ans = max(ans, total)
        return
    for j in range(N):
        if j not in lst:
            lst.append(j)
            # 해당 일을 했을 때의 확률을 곱해서 dfs 돌려주기
            dfs(i + 1, lst, total * (arr[i][j] / 100))
            # dfs 후, lst 에서 j 빼주기
            lst.pop()

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    dfs(0, [], 1)
    # 소수점 7번째에서 반올림해서 6번째까지 = :.6f
    print(f'#{tc} {ans*100:.6f}')