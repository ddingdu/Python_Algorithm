import sys
sys.stdin = open('../input.txt', 'r')

# MST를 구성하는 간선의 가중치를 모두 더해 출력

def prim(s, V):
    MST = [0] * (V+1)
    MST[s] = 1
    maxV = 0 # 최소신장트리 가중치의 합

    for _ in range(V): # V개 정점 연결
        u = 0   # 어떤 i랑 연결된 j 중에 최소 가중치를 가진 정점
        minV = 10000 # 연결된 정점 중 최소 가중치를 찾을 것


        for i in range(V+1):
            if MST[i] == 1: # MST 에 포함된 i 찾기
                for j in range(V+1):
                    # i와 j가 연결되어 있고, 트리에 포함 X, 새로 연결할 j가 최소 가중치를 가졌다면
                    if adjm[i][j] > 0 and MST[j] == 0 and minV > adjm[i][j]:
                        u = j # 새로 연결할 u는 j가 된다, u:다음에 연결할 정점(가중치 최소 상태)
                        minV = adjm[i][j]

        maxV += minV
        MST[u] = 1 # 가중치가 최소인 정점 u를 트리에 포함시키기

    return maxV

T = int(input())
for tc in range(1, T+1):

    V, E = map(int, input().split())
    adjm = [[0] * (V+1) for _ in range(V+1)] # 인접 행렬

    for _ in range(E):
        # s:시작, e:목표, w:비용
        s, e, w = map(int, input().split())
        # 가중치가 있는 무방향 그래프
        adjm[s][e] = w
        adjm[e][s] = w
    # print(adjm)
    ans = prim(0, V)
    print(f'#{tc} {ans}')
