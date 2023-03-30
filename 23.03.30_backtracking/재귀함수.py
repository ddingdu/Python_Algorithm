lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = 10
cnt = 0
# Q : 합이 10인 부분집합의 개수 구하기
# 현재 위치 idx에 대하여 idx번째 원소를 선택 or 선택 x
# s: 합
def recur(idx, s, selected):
    global cnt

    # 가지 치기
    # 지금(idx번째)까지의 합이 10보다 크면, 더이상 탐색할 필요가 없음
    if s > 10:
        return

   # 종료 조건
    if idx == n:
        if s == 10:
            cnt += 1
            # 지금까지 골랐던 수 출력
            print(selected)
        return

    # 재귀 호출
    # idx 번째 원소를 선택하거나
    selected.append(lst[idx])
    recur(idx + 1, s + lst[idx], selected)
    # idx 번째 원소를 선택하지 않거나
    selected.pop()
    # 선택하지 않았기 때문에 합(s)는 변화 없음
    recur(idx + 1, s, selected)

recur(0, 0, [])

