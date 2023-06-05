x = int(input())    # 총 금액
n = int(input())    # 물건 종류 수

lst = []    # 물건별 가격 담아줄 리스트

for _ in range(n):
    # a: 물건 가격, b: 물건 개수
    a, b = map(int, input().split())

    # 물건 종류(n)번 반복하면서 리스트에 물건별 총액 넣기
    for _ in range(n):
        lst.append(a * b)
        break

# 리스트 합이 총 금액과 일치하다면 'Yes'
if sum(lst) == x:
    print('Yes')
else:
    print('No')

''' 다른 풀이
x = int(input())
n = int(input())
ans = 0
for _ in range(n):
    # a: 물건 가격, b: 물건 개수
    a, b = map(int, input().split())
    ans += a * b

if ans == x : print('Yes')
else : print('No')
'''