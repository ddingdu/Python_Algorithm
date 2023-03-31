import sys
sys.stdin = open('../input.txt', 'r')
'''
임의의 위치에서 시작 = 모든 경우
4방향으로 6번 이동해서 7자리 수
격자판이 주어졌을 때, 만들 수 있는 서로 다른 7자리 수들의 개수
'''

def dfs(n,tst, ci, cj):
    if n == 7:
        sset.add(tst) # 중복제거
        return

    for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        ni, nj = ci + di, cj + dj
        if 0 <= ni < 4 and 0 <= nj < 4:
            dfs(n+1, tst + arr[ni][nj], ni, nj)

T = int(input())
for tc in range(1, T+1):
    arr = list(input().split() for _ in range(4))
    sset = set()

    for i in range(4):
        for j in range(4):
            dfs(1, arr[i][j], i, j)
    ans = len(sset)
    print(f'#{tc} {ans}')