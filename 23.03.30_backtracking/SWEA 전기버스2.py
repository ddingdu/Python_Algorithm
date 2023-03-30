'''
충전지마다 최대로 운행할 수 있는 정류장 수가 정해져 있음
최소한의 교체 횟수로 목적지 도착
'''
def solve(i):
    global charge, min_v

    if charge >= min_v:
        return

    if i >= len(lst):
        if min_v >= charge:
            min_v = charge
        return

    for i in range(i + lst[i], i, -1):
        charge += 1
        solve(i)
        charge -= 1

T = int(input())
for tc in range(1, T+1):
    lst = list(map(int, input().split()))
    N = lst[0]
    charge = 0
    min_v = 10000
    solve(1)

    print(f'#{tc} {min_v-1}')

