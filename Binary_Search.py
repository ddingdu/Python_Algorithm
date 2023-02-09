def binary_search(arr, n, key):
    start = 0
    end = n-1

    while start <= end:
        mid = (start+end) // 2
        if arr[mid] == key:
            print("Find")
            return mid
        elif arr[mid] > key:
            # 검색 범위를 재지정
            # 오른쪽은 더 이상 살펴 볼 필요가 없다(뒤는 어차피 나보다 큼)
            # 검색의 끝 범위를 가운데로 땡겨온다
            end = mid - 1
        else:
            # 검색 범위 재지정
            # 왼쪽은 더 이상 살펴 볼 필요가 없다(앞은 어차피 나보다 작음)
            # 검색의 끝 범위를 가운데로 땡겨온다
            start = mid + 1
    print("Can't Find")
    return -1

arr = [2, 3, 5, 7, 8, 16, 77] # 반드시 정렬 필요
n = len(arr)
print(binary_search(arr, n, 77))