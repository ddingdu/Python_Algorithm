# prime number < 소수 구하기 >
# 1부터 1000까지의 수중에 소수를 출력하시오
# 소수 : 1보다 큰 수 중에서 약수를 1과 자기 자신만 가지는 수(2빼고 다 홀수)

# 에라토스테네스의 체 (체 : 칸 안에 숫자를 하나씩 넣음)
# 1. 2부터 소수를 구하고자 하는 구간의 모든 수를 나열
# 2. 2는 소수이므로 2는 소수로 체크하고, 2를 제외한 자기 자신의 배수를 모두 소수가 아니라 체크
# 3. 다음 수로 이동(체크가 안된 수로), 3은 소수이므로 소수로 체크, 3을 제외한 자기 자신의 배수
# 4. 위의 과정을 반복하면 원하는 구간의 소수가 남게 된다.

# n의 소수 구하기
# prime = []
# for i in range(2, n+1):
#     # i를 기준으로 해서 i를 j로 나눴을 때 나머지가 0이면 배수 ==> 체크
#     # j의 범위는 2 <= j < i
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         prime.append(i)
# print(prime)
# # 소수 판별
n = 1000000    # 2부터 1000까지의 모든 수에 대하여 소수 판별
is_prime = [True for i in range(n + 1)] # 처음엔 모든 수가 소수인 것으로 초기화
for i in range(2, int(n ** 0.5) + 1):
    if is_prime[i]: # i가 소수인 경우
        # i를 제외한 모든 i의 배수를 지우면 된다 (False)로 체크
        j = 2
        while i * j <= n:
            is_prime[i * j] = False
            j += 1

print(is_prime[1:3])
print(is_prime[23])
# 0, 1 제외한 소수 개수
print(is_prime.count(True)-2)   # 1000000 넣었을 때 78498

# 최대 공약수 gcd (greatest common divisor)
# 최소 공배수 lcm (least common mutiple)
# a > b
'''
def gcd(a, b):
    # 뒤에서부터 둘다 나누어 떨어지는 것 찾아보기
    for i in range(b, 0, -1):
        if a % i == 0 and b % i == 0:
            return i

def new_gcd(a, b):
    if b == 0:
        return a
    else:
        return new_gcd(b, a % b)
    # a % b == 0
    # return b
    # else
    # gcd(b, a % b)

def lcm(a, b):
    return a * b // gcd(a, b)

a = 20
b = 15
print(gcd(a, b))    # 5
print(new_gcd(a, b))# 5
print(lcm(a, b))    # 60
'''