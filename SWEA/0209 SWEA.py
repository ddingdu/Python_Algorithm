# 고지식한 알고리즘(Brute Force)
'''
p = 'ab'
t = 'aaaabaaaabaaaab'
M = len(p)
N = len(t)

def BruteForce(p, t):
    i = 0
    j = 0
    while j < M and i < N:
        if t[i] != p[j]:
            i = i - j
            j = -1
        i = i + 1
        j = j + 1
    if j == M:
        return i - M
    else:
        return -1

print(BruteForce(p, t)) # 3
'''
'''
# 보이어 무어 알고리즘 # 고지식한 알고리즘보다 효율적임, 참고
def bm_search(txt, pat):
    ti = 0    # txt 인덱스
    pi = 0    # pat 인덱스

    n = len(txt)
    m = len(pat)

    skip = {}

    # 패턴 안에 있는 문자는 몇 칸 건너 뛸지 정해준다
    for p in pat:
        skip[p] = m - 1 - pat.rfind(p)
    # 만약 딕셔너리에 없는 경우는 그냥 패턴의 길이만큼 건너뛴다
    # (패턴에 없다는 뜻)
    print(skip)    # {'a': 4, 'b': 3, 'c': 2, 'd': 5, 'e': 1, 'f': 0}

    # 패턴의 제일 뒤 글자부터 비교
    ti = m-1

    while ti < n:
        pi = m - 1  # 패턴의 뒤에서붜 비교 시작

    # 같은 문자가 나오면 계속 앞으로 이동
    # 다른 문자가 나오면 건너뛰기 표를 참고해서 skip
        while txt[ti] == pat[pi]:
            if pi == 0:
                # 패턴의 맨 앞까지 와버리면, 뒤에 있는 글자가 모두 같았다.
                # 기준 위치인 ti를 리턴
                return ti
            ti -= 1
            pi -= 1
        # 건너뛰기 표에 있는 문자가 나오면 표에 적힌대로 skip
        # 건너뛰기 표에 없는 문자가 나오면 패턴의 길이만큼 skip

        # offset = skip[txt[ti]]  # skip이 딕셔너리이기 때문에 keyerror 발생
        offset = skip.get(txt[ti]) if skip.get(txt[ti]) else m

        # 다시 비교를 시작할 위치를 정해준다
        # 위에서 계산한 건너뛰기 만큼 이동
        ti += offset if offset > m - pi else m - pi
    return -1
t = "zzzabcdabcdabcefabcd"
p = "abcdabcef"
print(f"res : ", bm_search(t, p), t.find(p))    # 7 7
'''

# # 16370 글자수
# # s1에 포함된 글자들이 s2에 몇개씩 들어있는지 찾고, 그 중 가장 많은 글자의 개수
# # 'ABCA', 'ABABCA' # 3
# import sys
# sys.stdin = open("input.txt", "r")
#
# t = int(input())
# for tc in range(1, t+1):
#     s1 = input()
#     s2 = input()
#     # 빈 리스트 s1 길이만큼 ? ???
#     cnt = [0] * len(s1)
#     # s1 첫 글자 s2 순회하면서 cnt += 1
#     for i in range(len(s1)):
#         for j in range(len(s2)):
#             if s1[i] == s2[j]:
#                 cnt[i] += 1
#     print(f'#{tc}', max(cnt))

# 4698 테네스의 특별한 소수
# D 를 포함한 소수의 개수
# a 이상 b 이하
# str 로 변형해서 비교 ???

# 에라토스테네스의 체 사용해서 소수 체크 배열 만들기
# n = 10 ** 6
# is_prime = [True for i in range(n + 1)]
# is_prime[0] = False
# is_prime[1] = False
#
# for i in range(2, int(n ** 0.5) + 1):
#     if is_prime[i]:
#         j = 2
#         while i * j <= n:
#             is_prime[i * j] = False
#             j += 1
#
# t = int(input())
# for tc in range(1, t+1):
#     D, a, b = map(int, input().split())
#     cnt = 0
#     for i in range(a, b + 1):
#         if is_prime[i] and str(D) in str(i):
#             cnt += 1
#     print(f'#{tc} {cnt}')

# 5986 새샘이와 세 소수 - 시간 초과 유의
# 7=2+2+3 / 11=2+2+7 / 25=7+7+11
# 세 소수의 합으로 나타낼 수 있는 경우의 수
'''
primes = []
for i in range(2, 1000):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        primes.append(i)

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    cnt = 0
    # 소수가 몇 개인지
    prime_len = len(primes)
    # 경우의 수 모두 구하기
    # 중복 값 허용(같은 소수를 합에 사용 가능)되므로 범위 시작점 설정 유의
    for i in range(prime_len):
        for j in range(i, prime_len):
            for k in range(j, prime_len):
                if primes[i] + primes[j] + primes[k] == n:
                    cnt += 1
    print(f'#{tc} {cnt}')
'''


# 1215 회문1
# import sys
# sys.stdin = open("input.txt", "r")
#
# t = 10
# for tc in range(1, t+1):
#     w = int(input())  # 단어 길이
#     arr = [input() for _ in range(8)]
#     result = 0
#     for i in range(8):
#         # 단어 길이 만큼 순차적으로 반복
#         for j in range(8-w+1):
#             ans_1 = []
#             ans_2 = []
#             # 단어 길이 내에서 반복
#             for p in range(w):
#                 ans_1 += arr[i][j+p]
#                 ans_2 += arr[j+p][i]
#             if ans_1 == ans_1[::-1]:
#                 result += 1
#             if ans_2 == ans_2[::-1]:
#                 result += 1
#     print(f"#{tc} {result}")