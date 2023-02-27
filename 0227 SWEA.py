# 알고리즘 응용 1일차

import sys
sys.stdin = open('input.txt', 'r')


# 이진수2 (십진수를 이진수로 바꾸기)
'''
N = 0.625   ==>  0.101 (이진수)
= 1*2-1 + 0*2-2 + 1*2-3
= 0.5 + 0 + 0.125
= 0.625
'''
'''
t = int(input())
for tc in range(1, t+1):
    n = float(input())  # 실수 입력받기

    b = ''    # 실수를 이진수로 바꾼 결과
    cnt = 0    # 현재 내가 계산하고 있는 자릿수

    # 반복문을 돌면서 이진수로 바꾸기
    # 결과가 0 이면 반복 중단
    while cnt < 13 and n != 0:
        n *= 2
        cnt += 1

        # 원래 수 * 2를 한 결과가 1 이상 ==> 이진수에 1 추가
        if n >= 1:
            # 1을 빼주고 (정수 부분) 다음 계산을 이어나가기
            n -= 1
            b += '1'
        # 원래 수 * 2를 한 결과가 1 미만 == > 이진수에 0 추가
        else:
            b += '0'

    # 자릿수 13 이상이면 overflow
    if cnt < 13:
        ans = b
    else:
        ans = 'overflow'
    print(f'#{tc} {ans}')
'''

# < A 를 16 진수로 표현하기 >
# a = 'A'
# hex = int(a, 16)
# print(hex)    # 10

'''
3
4 47FE
5 79E12
8 41DA16CD
'''
# 이진수 (16진수를 4자리 2진수로)
# 16진수 ==> 2진수 * 4

# 47FE
# 4: 0100
# A(10): 1010 F(15): 1111
# 16진수 => 2진수 * 4   ==>  4: 0100 => 0400

t = int(input())
for tc in range(1, t+1):
    # n: 숫자 길이, hex_num: 16진수들
    n, hex_num = input().split()

    n = int(n)
    result = ''

    # 16진수를 10진수로
    for i in range(n):
        num = int(hex_num[i], 16)

        print()
        print(num, end = ' ')

        b = ''
        # 3 ~ 0번째 비트 검사해서 0 or 1
        for j in range(3, -1, -1):   # 내림차순으로 검사

            print(num & (2 ** j), end = ' ')

            # 10진수 숫자인 num 과 2 진수 비교 ????
            if num & (2 ** j) == 0:    # num 의 j번째 비트에 0이 있는지 검사
                b += '0'
            else:
                b += '1'
        result += b

    print(f'#{tc} {result}')