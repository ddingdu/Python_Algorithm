t = int(input())
for tc in range(1, t+1):
    n = int(input())
    # lambda 정렬 우선순위 : 1번 인덱스, 0번 인덱스
    doke = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x:(x[1], x[0]))
    # print(doke)
    cnt = 1
    # 0번 인덱스 값을 a, b로 설정
    a, b = doke[0]
    for i in range(1, n):
        if doke[i][0] >= b:
            cnt += 1
            # a, b 값 설정
            a, b = doke[i][0], doke[i][1]
    print(f'#{tc} {cnt}')
