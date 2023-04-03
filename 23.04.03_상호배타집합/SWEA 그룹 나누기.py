import sys
sys.stdin = open('input.txt', 'r')

# 집합 대표들을 리스트에 넣고 리스트 길이 구하기

# [1] 집합 초기화
def make_set(x):
    p[x] = x

# [2] x가 속한 집합의 대표를 얻는 연산
def find_set(x):
    if x == p[x]:
        return x
    else:
        return find_set(p[x])

# [3] 두 집합 합치기
# x 가 속한 집합과 y 가 속한 집합을 합치는 연산
# 집합의 대표를 앞에 나온 인자가 속한 대표로 정한다.
def union(x, y):
    # y 가 속한 집합의 대표 = x 집합의 대표로 설정
    p[find_set(y)] = find_set(x)

t = int(input())
for tc in range(1, t+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))

    ans = set() # 중복 제거
    p = [0] * (N+1)

    # 집합 초기화
    for i in range(1, N+1):
        make_set(i)
    # 2개 씩 끊어서 시작과 끝 정하기
    for i in range(M):
        start, end = lst[i*2], lst[i*2+1]
        # 두 집합 합치기
        union(start, end)

    for i in p[1:]:
        # 집합 대표들을 리스트에 넣기
        ans.add(find_set(i))

    print(f'#{tc} {len(ans)}')