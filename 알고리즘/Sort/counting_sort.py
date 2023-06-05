# cnt = [0]*5
# print(cnt)
#
# A = [1,2]
# for x in A:
#     cnt[x] += 3
# print(cnt)

# 0 <= data <= 4
# count = [0]*5
# D = [0,4,1,3,1,2,4,1]
# for i in D:
#     count[x] +=

# for i : 1 -> 4
#     count[i] <- count[i-1] + count[i]

# for i : 0 -> 7
#     count[i] > 0 and c[i+1] > 0 and c[i+2] > 0



# 카운팅 정렬 (오름차순)

def counting_sort_asc(A, B, k):
    # A : 정렬 대상 (0 to K)
    # B : 정렬 결과 # A,B 길이는 같음
    # k : 정렬 대상 중 최댓값
    # C : 카운트 배열 (원소의 개수를 세주고, 자리를 정해준다.)

    C = [0] * (k+1)

    # 1. 각 원소의 등장 횟수를 세준다.
    for i in range(len(A)):
        # A[i]의 등장 횟수를 증가 시켜준다. # 중복 될 수 있음.
        # C[A[i]] = A[i]의 등장 횟수
        C[A[i]] += 1

    # 2. 각 원소의 등장 횟수를 계산해서 내가 들어갈 자리의 위치를 구해준다.
    for i in range(1, len(C)):
        # i번째 원소의 앞에 몇개의 원소가 있는지 확인하면
        # i 번째 원소가 최소 몇번째부터 등장하게 되는지 (결과 배열의 자리를) 알 수 있게 된다.
        C[i] += C[i-1] # 제일 작은수가 앞에 나와야하기 때문에 앞에서부터

    # 3. 뒤에서부터 A를 확인하면서 자리를 확인하고 채워 준다.
    # 자리를 채울 때마다 1 감소시켜야 다음 원소가 들어올때 자리 중복이 안된다.
    for i in range(len(B)-1, -1, -1):
        # C[A[i]] => A[i]번째 원소가 들어갈 자리 (들어가기 전에 1 빼준다.)
        C[A[i]] -= 1
        # 정렬 결과 대상의 자리에 A[i]를 넣어준다.
        B[C[A[i]]] = A[i]

nums = [0,4,1,3,1,2,4,1]
result_asc = [0] * 8

counting_sort_asc(nums, result_asc, max(nums))

print(result_asc)



# 카운팅 정렬 (내림차순)
'''
def count_sort_dec(A,B,k):
    # A : 정렬 대상 (0 to K)
    # B : 정렬 결과 # A,B 길이는 같음
    # k : 정렬 대상 중 최댓값
    # C : 카운트 배열 (원소의 개수를 세주고, 자리를 정해준다.)

    C = [0] * (k + 1)

    # 1. 원소의 등장 횟수를 세준다.
    for i in range(len(A)):
        C[A[i]] += 1

    # 2. 자리를 계산하는데 내림차순
    for i in range(len(C)-2,-1,-1):
        C[i] += C[i+1]

    # 3. 뒤에서부터(len()-1) 원소의 자리를 찾아주면 된다.
    for i in range(len(B)-1,-1,-1):
        C[A[i]] -= 1
        B[C[A[i]]] = A[i]

nums = [0,4,1,3,1,2,4,1]
result_dec = [0] * 8

count_sort_dec(nums, result_dec, max(nums))

print(result_dec)
'''