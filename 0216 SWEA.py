import sys
sys.stdin = open('input.txt', 'r')

# 토너먼트 카드게임
# 재귀함수 사용 / 규칙 잘 찾아보기
'''
# a : left / b : right
def winner(a, b):
    if card[a] == 1:    # a 가 가위일 때
        if card[b] == 3 or card[b] == 1:
            return a
        else:
            return b

    elif card[a] == 2:    # a 가 바위일 때
        if card[b] == 1 or card[b] == 2:
            return a
        else:
            return b

    elif card[a] == 3:    # a 가 보일 때
        if card[b] == 2 or card[b] == 3:
            return a
        else:
            return b

def tournament(i, j):    # i : 인덱스 0번 / j :  인덱스 n-1번
    # 종료 조건 : 제일 작은 문제의 조건의 해답 구해서 return
    if i == j:
        return i
    # 재귀 호출 : 부분 문제
    a = tournament(i, (i+j)//2)
    b = tournament((i+j) // 2+1, j)   # ????
    return winner(a, b)

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    card = list(map(int, input().split()))
    # i : 인덱스 0번 / j :  인덱스 n-1번
    win = tournament(0, n-1)

    # win 결과 값이 인덱스 번호이므로 +1
    print(f'#{tc} {win+1}')
'''
'''
# < 과제 > 계산기 2
# 우선 순위 높은 곱셈이 먼저 계산되도록 설정
pri = {"+" : 1, "*" : 2}
t = 10
for tc in range(1, t + 1):
    _ = int(input())
    st = input()
    equ = ""
    stk = []

    # 후위 표기식 변환
    for ch in st:
        if ch.isdigit():  # 숫자인 경우
            equ += ch
        else:  # 연산자인 경우
            # 스택에 값이 있고, 현재 연산자의 우선순위가 스택 마지막 원소보다 작거나 같다면
            while stk and pri[ch] <= pri[stk[-1]]:
                # 마지막 원소 꺼내서 식에 넣어주기
                equ += stk.pop()
            # 스택에 값이 없거나, 현재 연산자의 우선순위가 크다면 스택에 push
            stk.append(ch)
    while stk:
        equ += stk.pop()

    # 후위 표기식 연산
    for ch in equ:
        # 숫자인 경우 push
        if ch.isdigit():
            stk.append(int(ch))  # int 로 받아주기
        else:
            p1 = stk.pop()
            p2 = stk.pop()
            if ch == "*":
                stk.append(p2 * p1)
            else:
                stk.append(p2 + p1)
    # # 스택에서 팝해서 출력
    # # 그냥 출력하면 리스트로 나옴
    print(f'#{tc} {stk.pop()}')
'''
'''
# 배열 최소 합 (방법1)
def backtracking(row, remain, now_sum):

    global min_sum
    # 0. 가지 치기
    if now_sum > min_sum:
        return

    # 1. 종료 조건
    if row == n and remain == 0:
        if min_sum > now_sum:
            min_sum = now_sum
        return

    # 2. 재귀 호출
    # 현재행 row에서 i번째 열에 있는 숫자를 선택할 수 있는가?
    for i in range(n):
        can_place = True
        # 세로에 선택한 열이 있는지 검사
        for j in range(row):
            if selected[j][i] == 1:
                can_place = False
                break
        # 놓을수 있는지 검사
        if can_place:
            # 놓을수 있으면 현재 위치에 놓고 다음 위치로 이동
            selected[row][i] = 1
            backtracking(row + 1, remain - 1, now_sum + board[row][i])
            # 다시 되돌려놓고 진행 할수 있도록 해준다.
            selected[row][i] = 0

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    # 최소합
    min_sum = 100
    # 보드만들기
    board = [list(map(int, input().split())) for _ in range(n)]
    # 내가 i,j 위치의 칸을 선택했다고 표시
    selected = [[0] * n for _ in range(n)]
    backtracking(0, n, 0)
    print(f"#{tc} {min_sum}")
'''


# 배열 최소 합 (방법2)
# n * n  배열 / 한줄에 숫자 하나씩 고르기 / 최소합

# 현재 i 번째 행에 대해서 j 번째 열을 골라서 합 만들어서 비교
def backtracking(i, now_sum):
    global min_sum

    # 0. 가지치기
    # 현재 내가 알고있는 합이 이전에 구해둔 최소합보다 크다면, 진행 종료
    if now_sum > min_sum:
        return

    # 1. 종료 조건 (행(i)과 배열크기(n) 같다면)
    if i == n:
        if now_sum < min_sum:
            min_sum = now_sum
        return

    # 2. 재귀호출
    # 0 ~ (n-1)번째 열 중에서 이전에 고른 적 없는 j 열 선택
    for j in range(n):
        # 고른적 없는 j 열이라면 1 저장
        if not select[j]:
            select[j] = 1
            # j 번째 열 골라서 합을 구한 다음, 다음 행(i+1)으로 진행
            backtracking(i+1, now_sum + arr[i][j])
            # 다시 돌아와서 이번 열 건너뛰고 다음 열로 진행하도록
            select[j] = 0

t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    # j 번째 열 골랐는지 확인하기 위한 0 배열, 1로 표시해줌
    select = [0] * n
    min_sum = 99999
    # 0 번째 행, 합이 0 인 상태로 시작
    backtracking(0, 0)

    print(f'#{tc} {min_sum}')