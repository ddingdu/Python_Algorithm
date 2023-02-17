# 부분집합 구하기
'''
# 0과 1로 표현
bit = [0, 0, 0, 0]
for i in range(2):
    bit[0] = i
    for j in range(2):
        bit[1] = j
        for k in range(2):
            bit[2] = k
            for l in range(2):
                bit[3] = l
                # 생성된 부분집합 출력
                print(bit)
print("=============")

# i는 원소, k는 개수
def f(i, k):
    if i == k:
        print(bit)
    else:
        bit[i] = 1
        f(i+1, k)
        bit[i] = 0
        f(i+1, k)
f(0, 4)
'''
# 신교수님 설명

numbers = [1, 2, 3, 4, 5]
# selected[i] == 1 => 내가 i 번째 원소를 부분집합에 포함 o
# selected[i] == 0 => 내가 i 번째 원소를 부분집합에 포함 x
selected = [0] * 5

n = len(numbers)

# 재귀 함수로 부분집합 구하기
# i 번째 원소를 부분 집합에 포함 할지 안할지 결정

def subset(i):

    # 1. 재귀 종료 조건
    if i == n:
        # n 개의 원소에 대해 선택을 끝냈다. ( 고르든지 말든지 )
        for j in range(n):
            if selected[j]:
                print(numbers[j], end=" ")
        print()
        print("==========")
        return

    # 2. 재귀호출
    # i 번째를 선택하고(부분집합에 포함) 다음 (i+1)번째 원소를 선택하러 가거나
    selected[i] = 1
    subset(i+1)
    # i 번째를 선택하지 않고(부분집합에 포함하지 않음) 다음 (i+1)번째 원소를 선택하러 가거나
    selected[i] = 0
    subset(i+1)

subset(0)

'''
numbers = [1, 2, 3, 4, 5]
# selected[i] == 1 => 내가 i 번째 원소를 부분집합에 포함 o
# selected[i] == 0 => 내가 i 번째 원소를 부분집합에 포함 x
selected = [0] * 5

n = len(numbers)
# 합이 x 보다 작은 부분집합만 구해야 한다면?
x = 6

# 재귀 함수로 부분집합 구하기
# i 번째 원소를 부분 집합에 포함 할지 안할지 결정

def subset(i, subsum):
    # 0. 다른 조건(최적화 조건)이 있는 경우
    if subsum >= x:    # x = 6 보다 작은거 구하려면 = 넣어서 같은 것도 빼줘야함 ???
        return

    # 1. 재귀 종료 조건
    if i == n:
        # n 개의 원소에 대해 선택을 끝냈다. ( 고르든지 말든지 )
        for j in range(n):
            if selected[j]:
                print(numbers[j], end=" ")
        print()
        print("==========")
        return

    # 2. 재귀호출
    # i 번째를 선택하고(부분집합에 포함) 다음 (i+1)번째 원소를 선택하러 가거나
    selected[i] = 1
    subset(i+1, subsum + numbers[i])
    # i 번째를 선택하지 않고(부분집합에 포함하지 않음) 다음 (i+1)번째 원소를 선택하러 가거나
    selected[i] = 0
    subset(i+1, subsum)

subset(0, 0)    # 시작 지점 : 0, 합 : 0
'''
'''
# < 순열 >
# i 번째와 누구를 바꿀 것인지 (순서 뒤죽박죽)

numbers = [1, 2, 3, 4, 5]
n = 5
# i 번째 원소의 자리를 바꿔가며 순열 생성
# 자리를 바꿀 수 있는 경우의 수

def perm1(i):
    global cnt1
    # 1. 종료 조건
    if i == n:
        cnt1 += 1
        print(numbers)
        return

    # 2. 재귀 호출
    # 현재 위치 i 에서 다른 위치 j 에 있는 숫자와 한번씩 다 바꿔보기
    # 이전에 i, j <==> j, i 바꾼거랑 똑같으니까 ~~~~???
    # 근데 위치를 바꾸지 않고 진행할 수도 있다. i == j 경우, 바꾸지 않고 다음 원소의 자리를 바꾸러 이동
    for j in range(i, n):
        # i 번째와 j 번째 위치를 바꾸고 진행
        numbers[i], numbers[j] = numbers[j], numbers[i]
        # 재귀 호출해서 다음 (i+1) 번째 원소의 자리를 바꾸러 간다.
        perm1(i+1)
        # i 번째와 j 번째 위치를 되돌려 놓고 다음 진행
        numbers[i], numbers[j] = numbers[j], numbers[i]

cnt1 = 0
perm1(0)
print(cnt1)
'''
'''
# < 순열 >
# i 번째 누구로 올지 (사전순)
numbers = [1, 2, 3, 4, 5]
n = 5
# i 번째의 자리를 누구로 할 것인가 선택하는 방법
# i 번째 자리가 누구인지 기억해야 하므로 배열 필요

def perm2(i, selected):
    global cnt2
    # 1. 종료 조건
    if i == n:
        cnt2 += 1
        print(selected)

    # 2. 재귀 호출
    # 현재 위치 i에 누구를 놓을 것인가 선택
    for j in range(n):
        # j 번째 원소를 놓은 적이 없다면, j 번째 원소를 i 위치에 놓기
        if numbers[j] not in selected:
            # i 위치는 j 번째 원소가 선택되었다.
            selected[i] = numbers[j]
            # i 위치의 주인을 정했으니 i+1 번째 위치의 주인을 정하러 간다
            perm2(i + 1, selected)
            # i 번째 위치의 j를 선택취소 하고 다음으로 이동
            selected[i] = 0

cnt2 = 0
perm2(0, [0] * 5)
print(cnt2)
'''























