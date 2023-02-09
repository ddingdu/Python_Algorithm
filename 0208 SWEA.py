# <문자열 뒤집기 함수>
# def str_reverse(string):
#     ret = ""
#     n = len(string)
#
#     # 빈 문자열 만들고 뒤에서부터 이어 붙이기
#     for i in range(n-1, -1, -1):
#         ret += string[i]
#     return ret
#
#     # 앞 뒤를 차례대로 바꾸는 방법
#     # s2 = list(string)
#     # for i in range(n//2):
#     #     s2[i], s2[n - i - 1] = s2[n - i - 1], s2[i]
#     # print(s2)
#     # return ret
#
# s = "abcdefg"
# print(str_reverse(s))
# #     f = string[-1]
#     string[0] = f
#     s = string[-2]
#     string[1] = s

# <문자열 비교 함수 만들기>
# def simple_strcmp(s1, s2):
#     # s1과 s2 의 아스키 코드 값을 비교해서 사전 순서 리턴
#     return ord(s1) - ord(s2)
# print(simple_strcmp("A", "G"))
# print(simple_strcmp("z", "a"))

# def simple_strcmp(s1, s2):
#     # s1과 s2 의 아스키 코드 값을 비교해서 사전 순서 리턴
#     return s1 < s2
# print(simple_strcmp("A", "G"))
# print(simple_strcmp("a", "z"))

# <문자열 숫자를 정수로 변환하기>
# str() 사용하지 않고, itoa()구현
# 양의 정수를 입력 받아 문자열로 변환하는 함수

# def atoi(s):
#     i = 0
#     for x in s:
#         i = i * 10 + ord(x)-ord('0')
#     return i
# 1
# 10+2
# 120+3

# s = '123'
# print(atoi(s))
#
# def itoa(num):
#     ret = ""
#     # 숫자 하나씩 떼와서 (일의 자리부터) 문자열로 바꾸기
#     while num > 0:
#         i = num % 10
#         ret += chr(ord('0') + i)    # ord('0') = 48
#         num //= 10  # 몫 저장
#     return ret[::-1]
#
# s = itoa(123)
# print(s)
# print(type(s))



# 문자열 비교
# 방법 1) A in B
# 방법 2) 반복문 [ZZABCZZ] 'ABC' 구하기, 맨 앞부터 3개짤라서 비교
#          인덱스 2개 써야함, 큰거 작은거
# T = int(input())
# for tc in range(1, T+1):
#     N = input()
#     M = input()
#     # N 이 M 안에 에 있으면 1 / 없으면 0
#     if N in M:
#         ans = 1
#     else:
#         ans = 0
#     print(f'#{tc} {ans}')

# 1989 초심자의 회문 검사
# 회문이면 1 아니면 0
# T = int(input())
# for tc in range(1, T+1):
#     word = str(input())
#     a = len(word)
#     mid = a//2
#
#     r_word = word[-mid:]
#
#     if word[:mid] == r_word[::-1]:
#         ans = 1
#     else:
#         ans = 0
#     print(f'#{tc} {ans}')

# 회문 - (토마토 기러기 같은 영어 알파벳)
# index 연산 & 문자열 뒤집기 실습 참고
# import sys
# sys.stdin = open("input.txt", "r")
#
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     strs = [input() for _ in range(N)]
#
#     for i in range(N):
#         # 단어 만큼 순차적으로 반복
#         for p in range(N - M + 1):
#             # 단어 길이 내에서 반복
#             ans_1 = []
#             ans_2 = []
#             for t in range(M):
#                 ans_1 += strs[i][p + t]
#                 ans_2 += strs[p + t][i]
#             if ans_1 == ans_1[::-1]:
#                 result = "".join(ans_1)
#             if ans_2 == ans_2[::-1]:
#                 result = "".join(ans_2)
#     print(f"#{tc} {result}")

# 1221 GNS - 카운팅 정렬
# cnt = [0] * 5
# a = [1,2]
# for i in a:
#     cnt[i] += 3
# # [0, 3, 3, 0, 0]

import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for _ in range(1, T+1):
    tc, N = input().split()    # N : 테스트 케이스 길이
    nums = list(input().split())
    num_dict = {'ZRO':0, 'ONE':1, 'TWO':2, 'THR':3, 'FOR':4, 'FIV':5, 'SIX':6, 'SVN':7, 'EGT':8, 'NIN':9}
    cnt_arr = [0] * int(N)

    # print(num_dict)
    # for i in nums:
    #     for j in num_dict.values():
    #         if i == j:
    #             cnt_arr[] += j










