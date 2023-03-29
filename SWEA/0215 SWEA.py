# Forth
# 후위 표기법을 스택으로 계산하기

# import sys
# sys.stdin = open('input.txt', 'r')
'''
def get_result(postfix):
    stack = []
    result = 0
    # num_cnt = 0    # 피연산자 개수
    # cnt = 0    # 연산자 개수

    # for i in postfix:
    #     if "0" <= i <= "9":
    #         num_cnt += 1
    #     else:
    #         cnt += 1
    # # 피연산자 개수가 연산자 개수 보다 많지 않다면 오류
    # if not num_cnt > cnt:
    #     return "error"

    for c in postfix:
        # 피연산자 만나면 스택에 넣기
        if "0" <= c <= "9":
            stack.append(int(c))
        # 연산자 만나면 피연산자 2개 꺼내서 계산
        elif c == ".":
            break

        else:
            # 피연산자 2개가 연산자 1개를 만나면 스택에는 결과가 1개
            if len(stack) >= 2:
                right = stack.pop()    # 우항 먼저
                left = stack.pop()

                if c == "+":
                    result = left + right
                elif c == "-":
                    result = left - right
                elif c == "*":
                    result = left * right
                elif c == "/":
                    result = left // right
                # 결과 값을 스택에 push
                stack.append(result)
            else:
                return "error"

    return stack.pop()

t = int(input())
for tc in range(1, t+1):
    postfix = input().split()
    # postfix = ls[:-1]

    print(f'#{tc} {get_result(postfix)}')
'''
# 미로 찾기
'''
# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(r, c, n):
    # 방문 기록 남길 배열
    visited = [[0]*n for _ in range(n)]
    stack = []

    while True:
        # r,c 좌표가 3 이라면 성공, 1반환
        if arr[r][c] == 3:
            return 1
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            # 좌표 범위 내이고, 1 (벽)이 아니고, 방문한 곳이 아니라면,
            if 0 <= nr < n and 0 <= nc < n and arr[nr][nc] != 1 and not visited[nr][nc]:
                # 방문 기록 남기기
                visited[nr][nc] = 1
                # 스택에 좌표 push
                stack.append((r, c))
                # 다음 위치로 출발점 바꿔주기
                r, c = nr, nc
                break
        else:
            # 스택에 값이 있다면, 하나 꺼내서 돌아가기
            if stack:
                r, c = stack.pop()
            # 값이 없다면, 중단 ( 갈 수 있는 길 다 감 )
            else:
                break
        # 탈출 실패
    return 0


t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]
    r, c = 0, 0

    for i in range(n):
        for j in range(n):
            # 출발지점 2 의 좌표 저장
            if arr[i][j] == 2:
                r, c = i, j
    print(f'#{tc} {dfs(r, c, n)}')
'''
'''
# 계산기 1
# 문자열을 후위 표기식으로 바꾸어 계산하기

t = 10
for tc in range(1, t+1):
    n = int(input())
    string = list(input())

    # 후위 표기식
    postfix = ""
    stack = []

    for i in range(n):
        if "0" <= string[i] <= "9":
            postfix += string[i]
        else:
            stack.append(string[i])
    while stack:
        postfix += stack.pop()
    # print(postfix, stack)

    # 후위 표기법을 스택으로 계산
    for c in postfix:
        if "0" <= c <= "9":
            stack.append(int(c))
        else:
            p1 = stack.pop()
            p2 = stack.pop()

            result = p1 + p2
            stack.append(result)
        ans = stack.pop()

    print(f'#{tc} {ans}')
'''
# 백트래킹

# 2806 N-Queen

# 4*4 체스판 퀸 4개 놓기
# remain : 남은 체스 말 ??
def backtracking(row, remain):
    #
    global cnt

    # 1. 종료 조건 : n 개를 다 놨을 때
    if row == n and remain == 0:
        cnt += 1
        return

    # 2. 재귀 호출

    # 현재 행 row 에서 i번째 열에 퀸을 놓을 수 있는가?
    for i in range(n):
        # 기본적으로 놓을 수 있다고 설정
        can_place = True
        # 세로에 퀸이 있는지 검사 (0부터 row 까지, row 위 값없으니까 반복문 종료됨)
        for j in range(row):
            if board[j][i] == 1:
                can_place = False
                break
        # 대각선에 퀸이 있는지 검사
        # 한 칸씩 올라가보기 : j
        for j in range(1, row+1):
            # 좌상
            # -j : 같은 만큼 빼지기 때문
            if row - j >= 0 and i - j >= 0 and board[row-j][i-j]:
                can_place = False
                break

            # 우상
            if row - j >= 0 and i + j < n and board[row-j][i+j]:
                can_place = False
                break

        # 놓을 수 있는지 검사
        if can_place:
            # 놓을 수 있으면 현재 위치에 놓고 다음 위치로 이동
            board[row][i] = 1
            backtracking(row + 1, remain -1)
            # row 의 i 번째에 있던거 빼기
            board[row][i] = 0

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    cnt = 0

    # 보드 만들기
    board = [[0] * n for _ in range(n)]
    backtracking(0, n)

    print(f'#{tc} {cnt}')

    # 2 1 2 입력 시, 1 0 출력
