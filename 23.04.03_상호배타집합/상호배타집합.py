# p[x] => x 의 부모
# p[x] == x => x의 집합 대표가 x이다. x는 대표자
p = [0] * 7

# [1] 집합 초기화
def make_set(x):
    p[x] = x

# [2] x가 속한 집합의 대표를 얻는 연산
def find_set(x):
    if x == p[x]:
        return x
    else:
        return find_set(p[x])

# [3] 두 집합을 합치는 연산
# x가 속한 집합과 y가 속한 집합을 합치는 연산
# 집합의 대표를 앞에 나온 인자가 속한 대표로 정한다.
def union(x, y):
    # 집합을 합치기 위해 필요한 것? : 대표
    p[find_set(y)] = find_set(x) # y가 속한 집합의 대표 = x 집합의 대표로 설정
for i in range(1, 7):
    make_set(i)

union(1, 3)
union(2, 3)
union(5, 6)

print(find_set(6)) # 5
print(find_set(5)) # 5
print(find_set(4)) # 4
print(find_set(3)) # 2
print(find_set(2)) # 2
print(find_set(1)) # 2
print(p) # [0, 2, 2, 1, 4, 5, 5]