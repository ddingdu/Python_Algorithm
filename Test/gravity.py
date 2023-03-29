import sys

sys.stdin = open("../23.03.29_분할정복/input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    # 가로 칸의 수
    n = int(input())

    # 상자 탑 높이 정보
    box = list(map(int, input().split()))

    # 초기값 정할 때: 최댓값 => 적당히 작은 값 / 최솟값 => 적당히 큰 값
    ans = 0

    # 반복문을 돌면서 현재 위치의 높이에서 제일 위에
    # 있는 상자의 낙차 중에 가장 큰 값 구하기
    for i in range(n):
        # 현재 위치에서 맨 꼭대기 상자가 오른쪽에 장애물 없다고 했을 때 최대 낙차 구하기
        height = n - (1 + i)  # n = 9
        # print(height)
        # 0 1 2 3 4 5 6 7 8
        # 8 7 6 5 4 3 2 1 0

        cnt = 0
        # 또 반복문을 돌면서 현재 '내 위치 기준', 오른쪽에 있는 장애물 수 구하기
        for j in range(i + 1, n):
            # 내 위치 (i) 기준 오른쪽 : i + 1
            # 현 위치 상자 높이 : box[i]
            # 현 위치 기준 오른쪽 상자 높이 : box[j]
            if box[i] <= box[j]:
                cnt += 1

    # 최대 낙차 = 현재 위치에서 오른쪽에 상자가 없을 경우 최대 낙차 - 오른쪽 상자수
        if ans < height - cnt:
            ans = height - cnt
    # 최대 낙차 중 최댓값을 갱신

    print(f"#{tc} {ans}")
