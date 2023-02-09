# '''
# 7
# 7 2 5 3 4 6 4
# '''
#
# N = int(input())
# arr = list(map(int, input().split()))
#
# for i in range(N-1):
#     minIdx = i
#     for j in range(i+1, N):
#         if arr[minIdx] > arr[j]:
#             minIdx = j
#     arr[minIdx], arr[i] = arr[i], arr[minIdx]
# print(arr)

# 맨 앞자리부터 자리의 주인을 정해준다. (최솟값)
# i = 0 : 제일 작은 수
# i = 1 : 두번째로 작은 수 ..

# 선택정렬
def selection_sort(arr, n):
    for i in range(n - 1):
        min_idx = i
        # i 의 뒤부터 비교를 시작하면서 최솟값을 찾는다.
        for j in range(i + 1, n):
            # 제일 작은 숫자의 인덱스 찾기
            if arr[min_idx] > arr[j]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

arr = [10, 40, 30, 50]
n = len(arr)
print(selection_sort(arr, n))


# # 내림차순 정렬
# def selection_sort_dec(arr, n):
#     for i in range(n - 1):
#         max_idx = i
#         # i 의 뒤부터 비교를 시작하면서 최댓값을 찾는다.
#         for j in range(i + 1, n):
#             # 제일 작은 숫자의 인덱스 찾기
#             if arr[max_idx] < arr[j]:
#                 max_idx = j
#
#         arr[i], arr[max_idx] == arr[max_idx], arr[i]
#
#
# arr = []
# n = len(arr)
#
# print(selection_sort_dec(arr, n))