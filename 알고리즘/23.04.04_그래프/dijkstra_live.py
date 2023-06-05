# 다익스트라
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

def dijkstra(s, V): # s:출발, V:마지막 정점 번호
    U = [0] * (V+1)    # U 최소 비용이 결정된 정점 집합
    # 정점 1개 결정됨(시작 s)
    U[s] = 1           # U = {s}

    # D 복사하는 작업?????
    for i in range(V+1):    # s에서 정점 i로 가는 비용
        D[i] = adjM[s][i]

    # while U != V : 남은 정점의 비용 결정
    N = V+1
    # 개수가 정해져 있으므로 for 문
    for _ in range(N-1):    # N-1 개 정점의 비용 결정
        # D[w]가 최소인 w 결정
        minV = INF
        w = 0
        for i in range(V+1):
            if U[i] == 0 and minV > D[i]:   # 남은 정점 i 중, 최소 찾기
                w = i    # i를 후보로 정함
                minV  = D[i]
        U[w] = 1    # 최소인 w는 최소 비용 D[w] 확정
        # w에 인접인 정점에 대해, 기존 비용 vs w를 거쳐가는 비용 비교
        for v in range(V+1):
            # w 인접 행렬 찾기
            # w에 인접인 v의 조건 : 자기 자신 제외하고 인접한 것만 남도록
            if 0 < adjM[w][v] < INF:    # 0: 자기 자신
                # 기존 비용 vs w 거쳐가는 비용 비교해서 작은 값 선택
                D[v] = min(D[v], D[w] + adjM[w][v])



INF = 10000 # 문제에 따라 다르게
V, E = map(int, input().split()) # 0~V번 정점, E:간선 수
adjM = [[INF] * (V+1) for _ in range(V+1)]
for i in range(V+1):
    adjM[i][i] = 0    # 자기 자신으로 가는 비용

for _ in range(E):
    u, v, w = map(int, input().split()) # u -> v, w 가중치
    adjM[u][v] = w

# print()
D = [0] * (V+1)
dijkstra(0, V)
print(D) # [0, 2, 3, 9, 6, 10]