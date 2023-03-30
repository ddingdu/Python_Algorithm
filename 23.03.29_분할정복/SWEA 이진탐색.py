'''
정수 N개, 정렬한 상태로 A애 저장

'''

import sys
sys.stdin = open('../input.txt', 'r')

# turn: 시작(0), 왼(1), 오(2)
def binary(l, r, key, turn):
    global cnt
    m = (l+r)//2

    if key == A[m]:
        cnt += 1
        return
    if l >= r:
        return
    if turn == 0:
        binary(l, m-1, key, 1)
        binary(m+1, r, key, 2)
    elif turn == 1:
        binary(m+1, r, key, 2)
    else:
        binary(l, m-1, key, 1)

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # 정렬해줘야 이진탐색 가능
    A = sorted(map(int, input().split()))
    B = map(int, input().split())
    cnt = 0

    for i in B:
        binary(0, N-1, i, 0)
    print(f'#{tc} {cnt}')





'''
# 반복문을 활용한 이진 탐색 구현
def binary_search(arr, target, start, end):
    while start <= end:
        # 중간 인덱스는 시작 인덱스와 마지막 인덱스 사이의 중간 인덱스
        # 몫만 구하기 위해 // 연산자 활용
        mid = (start + end) // 2

        # 중간 인덱스의 값이 타겟 데이터와 같은 경우 탐색 종료
        if arr[mid] == target:
            return mid

        # 중간 인덱스의 값이 타겟 데이터보다 큰 경우
        # 마지막 인덱스를 중간 인덱스의 한 칸 앞으로 이동
        elif arr[mid] > target:
            end = mid - 1

        # 중간 인덱스의 값이 타겟 데이터보다 작은 경우
        # 시작 인덱스를 중간 인덱스의 한 칸 뒤로 이동
        else:
            start = mid + 1

    return None


arr = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
n = len(arr)
# 찾으려는 값으로서 임의로 4로 설정
target = 4

# 시작 인덱스 및 마지막 인덱스를 전달인자로 할당
res = binary_search(arr, target, 0, n - 1)
print("{}번째에서 타겟 확인.".format(res + 1))
'''