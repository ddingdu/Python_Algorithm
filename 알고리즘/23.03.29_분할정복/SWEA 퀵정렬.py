def partition(A, l, r):
    # 피봇 정하기 (비교 대상) 제일 왼쪽 원소로
    p = A[l]
    # 피봇보다 작은거는 맨 왼쪽부터, 큰거는 맨 오른쪽부터
    i, j = l, r
    # i: 왼쪽에 있으면 안되는 친구의 위치 (피봇보다 큰거)
    # j: 오른쪽에 있으면 안되는 친구의 위치 (피봇보다 작은거)
    while i <= j:
        # 피봇보다 큰거를 왼쪽부터 찾기 시작
        while i <= j and A[i] <= p:
            # 현재 i 위치에 있는게 피봇보다 작으면 큰거를 찾아서 한 칸 뒤로 이동
            i += 1
        # 피봇보다 작은거를 오른쪽부터 찾기 시작
        while i <= j and A[j] >= p:
            # 현재 j 위치에 있는게 피봇보다 크면 작은거를 찾아서 한 칸 앞으로 이동
            j -= 1
        # 큰게 왼쪽에 있으면 안되고, 작은게 오른쪽에 있으면 안되니까 자리 교환
        if i < j:
            A[i], A[j] = A[j], A[i]

    # 반복이 끝나면, 작은 것과 큰 것이 다 제자리에 있다.
    # 피봇 위치를 정해준다.
    A[l], A[j] = A[j], A[l]
    # 피봇의 위치를 리턴
    return j

def quickSort(A, l, r):
    if l < r:
        # 분할하고 피봇의 위치를 구한다.
        s = partition(A, l, r)
        # 피봇위치를 정했으니 피봇 제외 왼쪽 정렬
        quickSort(A, l, s-1)
        # 오른쪽 정렬
        quickSort(A, s + 1, r)

T = int(input())
for tc in range(1, T+1):
    M = int(input())
    A = list(map(int, input().split()))
    mid = M // 2
    N = len(A)
    quickSort(A, 0, N-1)

    print(f'#{tc} {A[mid]}')