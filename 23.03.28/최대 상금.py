'''
순열 (교재 31p)

최대 자릿수: 6자리, 최대 교환 횟수: 10qjs
'''
import sys
sys.stdin = open('../input.txt', 'r')

def perm(cnt):
    global max_v

    # 종료 조건 : 교환 횟수를 다 사용 했다면 최대 상금 구하기
    if cnt == c:
        t = int(''.join(nums))
        max_v = max(max_v, t)
        return

    # 재귀 호출
    # 교환 횟수가 남아있다면? 카드 바꾸기
    # 이 문제에서는 동일한 위치에서 중복 교환을 허용하기 때문에
    # 자리 위치 2개(i, j)를 교환 마다 새로 정해 주어야 한다.
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            nums[i], nums[j] = nums[j], nums[i]
            perm(cnt + 1)
            nums[i], nums[j] = nums[j], nums[i]


T = int(input())
for tc in range(1, T+1):
    max_v = 0
    nums, c = input().split()
    nums = list(nums)
    c = int(c)

    # 결국 순열의 경우의 수와 같다
    # 자리르 바꾸는 횟수가 순열의 길이보다 더 커봤자 어차피 중복
    if c > len(nums):
        c = len(nums)
    perm(0)
    print(f'#{tc} {max_v}')