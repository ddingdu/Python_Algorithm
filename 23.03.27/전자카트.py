# 순열
def patrol(now, e_sum):
    global min_v

    # 지금까지 구한 에너지의 합이 내가 알고 있는 최소값보다 크면 더이상 진행할 필요x
    if e_sum >= min_v:
        return

    # 종료조건: 모든 방을 다 방문했으면 시작점으로 돌아간다
    if 0 not in v:
        min_v = min(min_v, e_sum + e[now][0])
        return

    # 현재 위치에서 갈수 있는 다음 방을 탐색
    # 내가 이전에 들른 적이 없는 방 선택
    for n_room in range(n):
        if n_room != now and v[n_room] == 0:
            # 다음 방으로 갔다고 체크하고 길을 찾는다
            v[n_room] = 1
            # 다음 방의 에너지양을 더해서 이용
            patrol(n_room, e_sum + e[now][n_room])
            # 다음 경우의 수를 위해서 다음 방 체크 해제
            v[n_room] = 0


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    e = [list(map(int, input().split())) for _ in range(n)]
    v = [0] * n
    # 첫 방문, 출발 시 방문했다고 처리
    v[0] = 1
    min_v = 10000
    patrol(0, 0)

    print(f"#{tc} {min_v}")