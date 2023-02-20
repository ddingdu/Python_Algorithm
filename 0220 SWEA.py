import sys
sys.stdin = open('input.txt', 'r')

# 회전

# n 개의 수열 / 맨 앞 숫자를 맨 뒤로 보내는 작업 m번
# 수열 맨 앞에 있는 숫자 출력
'''
t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    num = list(map(int, input().split()))
    # 큐 만들기
    q = [0] * 1000
    front = rear = -1

    # 큐에 숫자 리스트 넣기
    for i in num:
        rear += 1
        q[rear] = i

    front = 0 # 배열 첫번째 인덱스
    rear = len(num)-1 # 배열 마지막 인덱스

    for k in range(m):
        front += 1
        rear += 1
        q[rear] = q[k]
        if rear == front:
            print('공백')
        elif rear == n - 1:
            print('포화')
    print(f'#{tc} {q[front]}')
'''

'''
# 큐 삽입
def enq(data):
    global rear
    rear += 1
    q[rear] = data
# 큐 삭제
def deq():
    global front
    front += 1
    return q[front]

t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    num = list(map(int, input().split()))
    # 공백 큐 생성하기
    q = [0] * n
    # 초깃값 설정
    front = rear = -1
    # 큐에 숫자 리스트 다 넣기
    for number in num:
        enq(num)
    # 맨 앞 값을 뒤로 m 번 이동
    for _ in range(m % n + 1):
        deq()
    # 큐의 맨 앞 값 출력
    print(f'#{tc} {q[front]}')
'''

# 피자굽기

# n개 동시에 구울 수 있는 화덕
# 치즈가 모두 녹으면 꺼냄
# 한 바퀴 돌 때, 치즈 양 반으로 줄어듬 c // 2
# 치즈 0 되면 화덕에서 꺼내고, 그 자리에 남은 피자 넣기

t = int(input())
for tc in range(1, t+1):
    # n: 오븐 크기, m: 피자 개수
    n, m = map(int, input().split())
    pizza_ls = list(map(int, input().split()))
    # 다음에 꺼내올 피자의 번호 (꺼내올 때마다 하나씩 증가 += 1)
    next_i = 0

    # 오븐 전용 큐 (넣었다 뺐다)
    oven = [0] * 1000
    ofront = orear = -1

    # 오븐에 차례대로 피자를 넣기
    for i in range(n):
        # 피자를 넣기(나중에 꺼낼 때를 위해서 피자 번호도 같이 넣기)
        orear += 1
        oven[orear] = [i, pizza_ls[i]]
        next_i += 1    # i는 for문 돌면 끝나버리기 때문에 next_i 써주기
    # 오븐에 남아있는 피자 개수??
    remain = n
    # 마지막(rear)에 꺼낸 피자의 번호
    last_index = -1

    # 모든 피자의 치즈가 녹을 때까지 반복 (정확한 횟수 모르기 때문에 while 문)
    while True:
        # 피자를 꺼내서
        ofront += 1
        i, pizza = oven[ofront]

        # 치즈를 녹이고 c // 2
        pizza //= 2

        # 치즈가 0이 안되었다. => 다시 오븐에 넣기
        if pizza != 0:
            orear += 1
            oven[orear] = [i, pizza]

        # 치즈가 0이 되었다
        else:
            # 현재 오븐의 자리에 남은 피자 하나 꺼내서 넣기
            if next_i < m:
                orear += 1
                oven[orear] = [next_i, pizza_ls[next_i]]
                # 하나 꺼냈으니까 다음 피자 위치 바꿔주기
                next_i += 1
            # 넣을 피자가 없다.
            else:
                remain -= 1
                if remain == 0:
                    # 오븐에 남은 피자도 없는 상황이 온다.
                    # 현재 피자의 번호가 답이된다.
                    # 반복 종료
                    last_index = i
                    break
    print(f'#{tc} {last_index + 1}')
