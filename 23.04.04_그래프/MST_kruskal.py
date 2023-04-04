# MST 크루스칼
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

def find_set(x): # x가 속한 집합의 대표 리턴
    while x != rep[x]: # x == rep[x]까지
        x = rep[x]
    return x

def union(x, y): # y의 대표원소가 x의 대표원소를 가르키도록
    rep[find_set(y)] = find_set(x)


V, E = map(int, input().split())
edge = []
for _ in range(E):
    s, e, w = map(int, input().split())
    edge.append([w, s, e]) # w(가중치)를 기준으로 정렬하도록 앞에 두기

edge.sort()
rep = [i for i in range(V+1)] # 리스트 컴프리헨션(리스트를 직관적으로 생성) 사용

# 내가 지금까지 선택한 간선 개수
cnt = 0
# MST 가중치의 합
total = 0
# MST의 간선 수 N = 정점 수 -1
N = V + 1

for w, s, e in edge:
    # s 집합 대표와 e 집합 대표가 달라야 사이클이 생성 X
    if find_set(s) != find_set(e): # 두개의 대표가 달라야 더해줄 수 있다??
        cnt += 1
        union(s, e)
        total += w
        # MST 구성이 끝나면 종료
        if cnt == N - 1:
            break
print(total)    # 175