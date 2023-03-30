'''
4
124783
667767
054060
101123
# Lose Baby Gin Baby Gin Lose
'''

def f(i, k):
    global ans
    # 인덱스가 카드의 갯수와 같아질 때(재귀 종료조건)
    if i == k:
        runtri = 0    # 런과 트리플릿을 검사
        # 앞의 숫자 3개
        if (p[0] == p[1] == p[2]) or (p[0] +2 == p[1]+1 == p[2]):
            runtri += 1
        # 뒤의 숫자 3개
        if (p[3] == p[4] == p[5]) or (p[3] +1 == p[4] and p[4]+1 == p[5]):
            runtri += 1
        if runtri == 2:
            ans = 'Baby Gin'

    else:
        # 완전 탐색하기
        for j in range(k):
            if u[j] == 0:    # A[j]가 미사용이면 (=사용하지 않은 숫자 위치를 찾으면)
                u[j] = 1    # A[j]사용으로 표시

                # p[i]자리를 A[j]로 결정
                p[i] = A[j]
                f(i+1, k)   # p[i+1] 결정하러 이동
                u[j] = 0

T = int(input())
for tc in range(1, T+1):
    A = list(map(int, input()))
    ans = 'Lose'

    p = [0]*6       # 경우의 수가 나타나는 배열
    u = [0]*6       # used 배열
    f(0, 6)

    print(ans)
