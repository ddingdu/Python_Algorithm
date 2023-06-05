import sys
sys.stdin = open('../input.txt', 'r')

def dfs(n, sm):
    global ans

    # 가지 치기
    if ans <= sm:
        return

    if n > 12:  # 종료 조건 : 1년을 넘어가버리면
        # 1년 동안 결제한 비용을 그 전 비용과 비교해서 최소값 고르기
        ans = min(ans, sm)
        return

    dfs(n + 1, sm + day * lst[n]) # 일권
    dfs(n + 1, sm + mon) # 월권
    dfs(n + 3, sm + mon3) # 분기권
    dfs(n + 12, sm + year) # 연간권


T = int(input())
for tc in range(1, T + 1):
    day, mon, mon3, year = map(int, input().split())
    # 12월 이용 계획
    lst = [0] + list(map(int, input().split()))
    ans = 365 * 3000
    dfs(1, 0)    # 1월부터
    print(f'#{tc} {ans}')

    # s = [0] * 13
    # for i in range(1, 13):
    #     # 가능한 방법 중, i 달까지의 최소 비용
    #     s[i] = s[i - 1] + day * lst[i] # 일권
    #     s[i] = min(s[i], s[i - 1] + mon) # 월권
    #     if i >= 3:
    #         s[i] = min(s[i], s[i - 3] + mon3) # 분기권
    #     if i > 12:
    #         s[i] = min(s[i], s[i - 12] + year) # 연간권
    #
    # ans = s[12]
    # print(f'#{tc} {ans}')