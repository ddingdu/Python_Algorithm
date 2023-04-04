# 다익스트라
# 시작 정점에서 거리가 최소인 정점을 선택해 나가면서 최단 경로 구하는 방식
# 트리 만들 필요 x
# 최단 경로를 계속 구하기 때문에 MST의 prim 알고리즘과 유사함
'''
5 8
0 1 2
0 2 4
1 2 1
1 3 7
2 4 3
3 4 2
3 5 1
4 5 6
'''

# s:시작 정점
def dijkstra(s, V):
    U = [0] * (V+1)
    U[s] = 1 # 최소 비용이 결정된 정점(시작 s) 표시
    D[s] = 0 # 출발점 비용을 결정

    # s 와 연결된 곳을 살펴보고 최소 비용 최신화
    # s 와 연결된 e번 정점, 가중치 w에 대해서
    for e, w in adjl[s]:
        D[e] = w # 무한대기 때문에 min 함수 안써도 w가 가장 작다??????\

    # 남은 정점의 비용을 결정
    for _ in range(V):
        # 비용이 아직 결정되지 않는 t 정점을 찾자
        # 그중에 D[t] 최소인 t를 찾기
        minV = INF
        t = 0   # 아직 찾지 않은 상태
        for i in range(V+1):
            #
            if U[i] == 0 and minV > D[i]:
                minV = D[i]
                t = i
        # 최소인 t를 찾았다
        U[t] = 1

        # 이전까지 알고 있던 비용(D[e])과 새로 경로가 만들어 졌을 때 비용(D[t] + w)
        # 그 중에서 최소값을 선택해서 최신화
        for e, w in adjl[t]:
            D[e] = min(D[e], D[t] + w) # D[e]:s에서 e까지 가는 ???비용?맞나?

# 무한대 값 필요 (문제마다 달라짐)
INF = 10000

V, E = map(int, input().split())
adjl = [[] for _ in range(V+1)] # 인접 리스트
for _ in range(E):
    s, e, w = map(int, input().split())
    adjl[s].append([e, w])

# D[i]는 시작 정점 a에서 i까지 가는데 걸리는 최소 비용
D = [INF] * (V+1)

dijkstra(0, V)
print(D)    # [0, 2, 3, 9, 6, 10]