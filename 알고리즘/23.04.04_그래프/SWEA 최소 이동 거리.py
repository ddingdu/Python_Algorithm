import sys
sys.stdin = open('../input.txt', 'r')

# 0번부터 V번까지 이동하는데 최소 거리 얼마인가
# 모두 방문해야 하는 것은 x

def dijkstra(s, V):
    U = [0] * (V+1)
    U[s] = 1 # U:최소 비용이 결정된 정점 방문 표시
    D[s] = 0 # D:출발점 비용을 결정

    # s 와 연결된 곳을 살펴보고 최소 비용 최신화
    # s 와 연결된 e번 정점, 가중치 w에 대해서
    for e, w in adjl[s]:
        D[e] = w

    # 남은 정점의 비용 결정
    for _ in range(V):
        # 비용이 결정되지 않은 t 정점 중 D[t] 최소인 t를 찾기
        minV = INF
        t = 0   # 아직 찾지 않은 상태
        for i in range(V+1):
            if U[i] == 0 and minV > D[i]:
                minV = D[i]
                t = i
        U[t] = 1   # 최소인 t

        # 기존 비용(D[e])과 새로 경로의 비용(D[t] + w) 중 최소값을 선택해서 최신화
        for e, w in adjl[t]:
            D[e] = min(D[e], D[t] + w)

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())

    adjl = [[] for _ in range(V + 1)]  # 인접 리스트
    INF = 10000

    for _ in range(E):
        s, e, w = map(int, input().split())
        adjl[s].append([e, w])

    D = [INF] * (V + 1)
    dijkstra(0, V)
    ans = D[V]

    print(f'#{tc} {ans}')