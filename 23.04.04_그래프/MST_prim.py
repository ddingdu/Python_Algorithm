# MST의 prim 알고리즘
# 하나의 정점에서 연결된 간선들 중에서 하나씩 선택하면서 MST를 만들어 가는 방식
# 중복 선택하지 않기 위해, 트리 정점과 비트리 정점 정보 유지
# 가중치 살펴보면서 최소인 것만 선택
'''
6 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
'''
# s:시작 정점 V:정점 개수
def prim(s, V):
    MST = [0] * (V+1) # MST 포함 여부
    MST[s] = 1
    # 최소 신장트리 가중치의 합
    maxV = 0
    # V번 반복하는 이유? V개 정점을 연결하기 위함
    for _ in range(V):
        u = 0   # 아직 정해지지 않은 상태 u, 어떤 i랑 연결된 j중에 최소 가중치를 가진 정점
        minV = 10000    # 연결된 정점 중 최소 가중치를 찾을 것

        # MS T에 포함된 정점 i와 인접한 정점 j 중에서 MST 에 포함되지 않고
        # 가중치가 최소인 정점 u를 찾기
        for i in range(V+1):
            # MST에 포함된 i 찾기
            if MST[i] == 1:
                for j in range(V+1):
                    # adjm[i][j] > 0 : i와 j가 연결되어 있다
                    # (0 이면 연결이 안된 상태라는 의미이므로 살펴볼 필요 없음)
                    # MST[j] == 0 : 지금까지 만든 트리에 포함이 안된 상태
                    # minV > adjm[i][j] : 새로 연결할 j는 최소 가중치를 가져야 한다.
                    if adjm[i][j] > 0 and MST[j] == 0 and minV > adjm[i][j]:
                        # u: 다음에 연결할 정점(가중치가 최소인 상태)
                        # 새로 연결할 u는 j가 된다
                        u = j
                        minV = adjm[i][j]
        maxV += minV
        # 가중치가 최소인 정점 u를 트리에 포함시키기
        MST[u] = 1

    return maxV


V, E = map(int, input().split())
adjm = [[0] * (V+1) for _ in range(V+1)]    # 인접 행렬


for _ in range(E):
    # s:시작 e:목표 w:비용
    s, e, w = map(int, input().split())
    # 가중치가 있는 무방향 그래프
    adjm[s][e] = w
    adjm[e][s] = w

print(prim(0, V))    # 175