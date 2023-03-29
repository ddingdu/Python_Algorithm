'''
5
55 7 78 12 42
for i : N-1 -> 1    # 각 구간의 끝
    for j : 0 -> i-1    # 비교할 왼쪽 원소의 인덱스
        if arr[j] > arr[j+1]
            arr[j] <-> arr[j+1] # 큰 원소 오른쪽으로

'''
'''
N = int(input())    # 입력 크기
arr = list(map(int, input().split()))
for i in range(N-1, 0, -1): # 각 구간의 끝
    for j in range(i):  # 비교할 왼쪽 원소
        if arr[j] > arr[j+1]:
            #  큰 원소 오른쪽으로
            arr[j], arr[j+1] = arr[j+1], arr[j]

print(*arr)
'''
N = 5
a = 55 7 78 12 42

def BubbleSort(a, N):   # 정렬할 List, N 원소 수
    for i in range(N-1, 0, -1): # 범위의 끝 위치
        for j in range(0, i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                return









