#2738 행렬 덧셈

import sys

sys.stdin = open("input.txt", "r")

# N * M 크기의 두 행렬 A, B 두 행렬 더하기
# N, M <= 100, |A, B| <= 100
N, M = map(int, input().split())
A = list(map(int, input().split()))
print(N, M)
print(A)

3 3
1 1 1
2 2 2
0 1 0
3 3 3
4 4 4
5 5 100