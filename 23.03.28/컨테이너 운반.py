import sys
sys.stdin = open('../input.txt', 'r')
'''
T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    wi = list(map(int, input().split()))
    ti = list(map(int, input().split()))

    wi = sorted(wi, reverse=True)
    ti = sorted(ti)
    print(wi, ti)
    ans = 0
    for t in range(m):
        for w in range(len(wi)):
            if ti[t] >= wi[w]:
                ans += wi[w]
                wi.pop(w)
                break
    print(f"#{tc} {ans}")
'''

# 교수님 풀이
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     w = list(map(int, input().split()))
#     t = list(map(int, input().split()))
#
#     # greedy? 큰 컨테이너부터 선택
#     w.sort(reverse=True)
#     t.sort(reverse=True)
#
#     # 다음에 이동할 컨테이너, 트럭의 인덱스
#     wi, ti = 0, 0
#     # 옮긴 화물의 총 중량
#     ans = 0
#     # 트럭을 보낼 수 있을 때까지
#     while wi < N and ti < M:
#         # 현재 옮길 차례의 화물이 트럭에 실을 수 있다면, 총 중량 증가
#         if w[wi] <= t[ti]:
#             ans += w[wi]
#             wi += 1
#             ti += 1
#         # 트럭이 작아서  wi 번째 화물을 못 옮길 경우
#         else:
#             wi += 1
#         print(ans)
#     print(f'#{tc} {ans}')