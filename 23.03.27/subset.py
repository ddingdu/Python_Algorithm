def f(i, k):
    if i == k:
        print(*bit)
    else:
        bit[i] = 0
        f(i+1, k)
        bit[i] = 1
        f(i+1, k)

A = [7, 2, 5, 3, 4]
N = len(A)
bit = [0] * N    # bit[i] A[i]원소가 부분집합에 포함되는지를 표시함
f(0, N)