# ''' 순열 '''
# # r이 3개로 고정
# N = 10
# for i in range(N-2):
#     for j in range(i+1, N-1):
#         for k in rnage(j+1, N):
#             print(i, j, k) # 10P3 => 120개 나옴


'''
조합 구하는 방법 2가지
1. idx번째 고를지 말지 (연습문제 3번 해보기!)
2. ? ? ?
'''

lst = [1, 2, 3, 4, 5]
N = 5
R = 3

# N개 중에 R개 고르는 경우의 수
# 1-1. idx 번째 숫자를 고를지 고르지 않을지 결정
def comb(idx, r, selected):
    # 재귀 종료조건
    # 마지막 번째 숫자를 고를지 말지 선택한 후, 종료
    if idx == N:
        print(selected)
        return
    # 재귀 호출
    # 고르고 진행하던가
    selected.append(lst[idx])
    comb(idx + 1, r + 1, selected)
    # 고르지 않고 진행하던가
    selected.pop()
    comb(idx + 1, r, selected)

comb(0, 0, [])

# 길이 R인 것만 출력
# 1-2. idx 번째 숫자를 고를지 고르지 않을지 결정
def comb(idx, r, selected):
    # 재귀 종료조건
    # 마지막 번째 숫자를 고를지 말지 선택한 후, 종료
    if idx == N:
        if r == R:
            print(selected)
        return
    # 재귀 호출
    # 고르고 진행하던가
    selected.append(lst[idx])
    comb(idx + 1, r + 1, selected)
    # 고르지 않고 진행하던가
    selected.pop()
    comb(idx + 1, r, selected)

comb(0, 0, [])


# 2. R개 고를 때까지 계속 선택
# 내가 idx 번째 원소를 골랐다면, idx 이전에 있는 친구는 고려하지 않고 뒤에 있는 것만 선택

def comb2(idx, selected):
    if len(selected) == R:
        print(selected)
        return

    for i in range(idx, N):
        comb2(i+1, selected + [lst[i]])

print("==========")
comb2(0, [])