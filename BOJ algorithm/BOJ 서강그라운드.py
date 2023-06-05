'''
5 5 4
5 7 8 2 3
1 4 5
5 2 4
3 2 3
1 2 3

23
'''

'''
각 지역 일정한 길이로 다른 지역과 양방향 연결 1 <= l <= 15
낙하지역 중심으로 1 <= m <= 15 이내 모든 지역의 아이템 습득 가능
얻을 수 있는 아이템 최대 개수
'''

import sys
input = sys.stdin.readline

import heapq   # 우선순위 큐
INF = int(1e9) # 무한대로 최댓값 설정

# n: 지역의 수, m: 최대 이동 가능 거리, r: 도로의 수
n, m, r = map(int, input().split())

# 각 지역 아이템 수를 리스트로 저장
items = list(map(int, input().split()))

# 각 지역 연결 정보와 길의 길이 그래프에 저장
graph = [[] for _ in range(n + 1)]
for _ in range(r):
    a, b, i = map(int, input().split())
    # 양방향 연결
    graph[a].append((b, i))
    graph[b].append((a, i))

# 얻을 수 있는 아이템 수
ans = 0 

def dijkstra(start):
    cnt = 0
    q = []
    heapq.heappush(q, (0, start))  # 시작 지점 큐에 삽입
    distance[start] = 0 # 거리 기록

    while q:
        dist, now = heapq.heappop(q)  # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기

        if distance[now] < dist:  # 현재 노드가 처리된 적 있는 노드라면 무시
            continue

        cnt += items[now - 1]  # 아이템 수 합산
        for i in graph[now]:  # 현재 노드와 연결된 다른 노드 확인
            cost = dist + i[1]  # 현재 노드에서 연결된 노드로 가는 거리 계산

        
            if cost <= m and cost < distance[i[0]]:    # 최단 거리보다 짧은 경우
                # 해당 노드까지의 최단 거리를 업데이트하고 큐에 삽입
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))  
    return cnt

# 모든 지점을 시작점으로 다익스트라 알고리즘 수행
for i in range(1, n + 1):
    distance = [INF] * (n + 1)  # 최단 거리 초기화
    ans = max(ans, dijkstra(i))  # 가장 많은 아이템을 얻을 수 있는 경우 찾기
print(ans)