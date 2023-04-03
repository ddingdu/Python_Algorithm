# 싸피 로봇

# i 현재 방의 번호
# s 지금까지 사용한 배터리 양
# selected 지금까지 들렀던 방 번호

def solve(i, s, selected):
    global min_v

    # 가지치기
    if s > min_v:
        return

    # 문제 조건 : b를 a 보다 먼저 방문하면 안된다.
    if a not in selected and b in selected:
        return

    # 종료 조건
    if len(selected) == n:
        # 처음 방으로 돌아가야 한다.
        min_v = min(min_v, s + arr[i][0])
        return

    # 재귀 호출
    # 내가 지금까지 들르지 않았던 방을 골라서 가면 된다.
    for next in range(n):
        if next not in selected:
            solve(next, s + arr[i][next], selected + [next])

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    # arr[i][j] = i번 방에서 j번 방으로 가는데 사용하는 배터리 양
    arr = [list(map(int, input().split())) for _ in range(n)]
    a, b = map(int, input().split())

    min_v = 10000

    solve(0, 0, [0])
    print(f'#{tc} {min_v}')


# gold_gyu

# def f(idx, lst, s):
#
#     global minV
#
#     # 종료조건
#     # 다시 사무실로 되돌아올 때, 즉, 모든 강의실을 다돌았을 때 + 마지막으로 사무실로 돌아왔을 때
#     if len(lst) == n and lst[-1] == 0:
#         # 정답처리
#         minV = min(minV, s)
#         return
#
#     # b지점은 일단 먼저 못간다.
#     # b지점이 아닌 곳들을 다 가보고
#     # 그다음에 a지점을 가본다.
#
#     for j in range(n):  # 사무실 ~ 강의실 선택지를 준다.
#         if j != idx:    # 행과 열이 같지 않고
#             if j not in lst:    # 가본적없는 강의실이고(중복되지않는)
#                 if a not in lst:    # a 또한 간적이 없다면
#                     # b를 갈 수 없다.
#                     if j == b:  # b를 가야한다면
#                         continue    # 안가고
#                 # a를 가봤다면 이제 b도 갈 수 있기 때문에 다른 제한은 없음
#                 f(j, lst + [j], s + arr[idx][j])    # 다음 꺼 찾음
#
#
# T = int(input())
#
# for tc in range(1, T+1):
#     n = int(input())
#     arr = [list(map(int, input().split())) for _ in range(n)]
#     a, b = map(int, input().split())
#     minV = n * 100
#
#     f(0, [], 0)
#     print(f"#{tc} {minV}")