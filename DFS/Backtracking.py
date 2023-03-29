# 백트래킹

# N-Queen

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

    # 2 1 2 입력 시, 1 0 출력력