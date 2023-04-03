# 연속한 1의 개수 찾기
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    m = input()

    # [1] 16진수를 10진수로, 10진수를 2진수로 바꾸기
    bin = ""    # 2진수 결과 담을 변수
    for s in m:
        # 16진수를 10진수로 바꾸기
        s = int(s, 16)
        # 4비트 씩 나눠서 2진수로 바꾸기
        for i in range(3, -1, -1):
            bin += "1" if s & (1 << i) else "0"

    # [2] 연속하는 1 세기
    cnt = 0
    # cnt 값 담아줄 빈 리스트
    lst = []

    # 2진수 하나씩 살펴보기
    for j in bin:
        # 1 만나면 cnt +1
        if j == "1":
            cnt += 1
        # 0 만나면 cnt 값 초기화
        else:
            cnt = 0
        # 리스트에 cnt 값들 담아주기
        lst.append(cnt)
    # 리스트에서 가장 큰 값을 정답 처리
    print(f'#{tc} {max(lst)}')