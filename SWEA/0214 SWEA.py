# 재귀함수
'''
def function1(num):
    print("now", num)
    # 1. 반드시 종료 조건을 정한다
    if num == 0:    # num == 20
        return
    # 2. 종료 조건이 아닌 경우 재귀 호출
    # 언젠가는 종료 조건을 만족하도록 변경 해줘야한다.
    else:
        function1(num-1)    # num + 1
    print("back", num)
function1(5)
# 실행흐름 5-4-3-2-1-0-1-2-3-4-5
# back 0 이 호출되지 않은 이유??? return 때문에 끝나서 ???
# now 5 다음에 왜 back 4 아닌지 ???

# 팩토리얼 재귀함수
def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)
print(fact(5))   # 120

# 피보나치 재귀함수
def fibo(n):
    if n < 2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)
print(fibo(7))    # 13

# Memoization(메모이제이션) - 미리 저장해놓고 가져다 쓰기 / 실행시간 줄일 수 있음

def fibo1(n):
    # global memo  # memo 수정해야 돼서 전역변수로 만들어둠

    # n 번째 항을 계산한 적이 없고, n 이 2 이상이라면
    # n 번째 항을 계산해야 된다.
    if n >= 2 and memo[n] == 0:
        memo[n] = fibo1(n-1) + fibo1(n-2)
        # print(memo[n])
    # 계산한 적이 있으면, memo[n] 값을 그대로 사용하면 된다.
    return memo[n]
n = 20
memo = [0] * 20
# memo[0] = 0
memo[1] = 1
print(fibo1(7))    # 13
'''

import sys
sys.stdin = open('../23.03.29_분할정복/input.txt', 'r')

# 그래프 경로
# 경로 있으면 1, 없으면 0

def dfs(start, end):
    stack = []
    visited = [0] * (v+1)
    stack.append(start)
    # start 부터 시작, 값이 있고, 아직 방문하지 않은 정점이면 stack 에 추가
    while stack:
        i = stack.pop()
        visited[i] = 1
        for w in range(v+1):
            if not visited[w]:
                if arr[i][w]:
                    stack.append(w)
    # end 지점을 방문하였는지 반환
    return visited[end]

t = int(input())
for tc in range(1, t+1):
    # 정점:v 간선:e
    v, e = map(int, input().split())
    arr = [[0]*(v+1) for _ in range(v+1)]
    # arr 에 입력받은 연결된 정점 표시
    for _ in range(e):
        x, y = map(int, input().split())
        arr[x][y] = 1
    result = 1
    # 입력 받은 a, b에 연결 되어있는지 확인
    a, b = map(int, input().split())
    if not dfs(a, b):
        result = 0
    print(f'#{tc} {result}')

'''
# 재만풀이
# 1-4 가능, 4-1 불가능
def dfs(S):
    stack.append(S)
    for i in arr[S]:
        if not visited[i]:
            visited[i] = 1
            dfs(i)

t = int(input())
for tc in range(1, t+1):
    # V:노드 개수, E:간선 개수
    V, E = map(int, input().split())
    arr = [[] for _ in range(V + 1)]
    visited = [0] * (V+1)
    stack = []
    for _ in range(E):
        start, end = map(int, input().split())
        arr[start].append(end)

    # 간선 개수 E 만큼 반복해서 입력 받은 뒤
    # 경로 존재 확인할 출발 노드:S, 도착 노드:G
    S, G = map(int, input().split())

    visited[S] = 1
    dfs(S)
    if G in stack:
        ans = 1
    else:
        ans = 0

    print(f'#{tc} {ans}')
'''
# 종이붙이기
'''
def paper(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3
    # 2를 표현하는 방법은 2개이므로 (n-2)일 때는 *2
    # f(n) = f(n-1) + f(n-2)*2
    return paper(n-1) + paper(n-2) * 2

t = int(input())
for tc in range(1, t+1):
    n = int(input()) // 10 # n = 1,2,3,4,,,
    print(f'#{tc} {paper(n)}')
'''