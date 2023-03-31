import sys
sys.stdin = open('../input.txt', 'r')
'''
정해진 칼로리 이하의 조합 중에서 가장 선호하는 햄버거 조합
같은 재료 중복 X
'''
# idx:현재 재료 번호/score:지금까지 점수 합/kal:지금까지 칼로리 합
def solve(idx, score, kcal):
    global max_s

    # 남은 점수 다 합해도 최대보다 작으면 진행 x
    # 남은 점수 개념 헷갈림 !!!
    remain = 0
    for i in range(idx, N):
        remain += foods[i][0]

    if score + remain < max_s:
        return

    # kal 이 L 보다 크면 진행 x
    if kcal > L:
        return

    # 종료 조건
    if idx == N:
        max_s = max(max_s, score)
        return

    # idx 번째 재료를 선택하거나 안하거나
    solve(idx + 1, score + foods[idx][0], kcal + foods[idx][1])
    solve(idx + 1, score, kcal)

T = int(input())
for tc in range(1, T + 1):
    # N:재료 수, L:제한 칼로리
    N, L = map(int, input().split())
    # [0]:점수, [1]:칼로리
    foods = [list(map(int, input().split())) for _ in range(N)]
    max_s = 0
    solve(0, 0, 0)
    print(f'#{tc} {max_s}')