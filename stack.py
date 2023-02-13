# 1. 배열의 메서드 사용하기

stack = []

def push(item):
    stack.append(item)

def pop():
    if len(stack) == 0:
        return
    else:
        return stack.pop()

def peek():
    return stack[-1]

for i in range(10):
    push(i)

print(stack)
print(peek())

for i in range(10):
    print(pop(), end=" ")
print()


# 2. 스택 직접 구현하기

# 스택 초기화
stack = [0] * 10
size = 10
top = -1

def my_push(item):
    # push 를 하고 나면 꼭대기인 top 변수가 변하기떄문에 global 선언
    global top

    if top == size:
        print("가득참(오버플로우)")
        return
    else:
        top += 1
        stack[top] = item

def my_pop():
    global top
    if top == -1:
        print('언더플로우')
        return
    else:
        top -= 1
        return stack[top + 1]
for i in range(10):
    my_push(i)
print(stack)

for i in range(10):
    print(my_pop(), end=" ")
print()

# < 연습문제 2 > 16p 괄호의 짝을 검사하는 프로그램 작성
# bracket (괄호)
'''
4
( )( )((( )))   # 첫 케이스만 짝 맞음 (1)
((( )((((( )( )((( )( ))((( ))))))
())
(()
'''
'''
# 스택을 이용한 괄호 검사
t = int(input())
for tc in range(1, t+1):
    row = input() # 검사할 문자열
    stack = []
    answer = 1 # 괄호가 제대로 되어있다, 0 => 제대로 되어있지 않다

    for c in row:
        # 열린 괄호가 나오면 스택에 push
        if c == "(":
            stack.append(c)
        # 닫힌 괄호가 나오면
        # 스택 길이가 0 이 아닌지 검사 (언더플로우 방지)
        # 스택에서 pop 해서 나온 괄호와 짝이 일치하는지 검사
        if c == ")": # 첫 인덱스에 닫힌 괄호 들어오면
            if len(stack) == 0: # 0 은 첫 인덱스라는 뜻
                answer = 0
                break # 인덱스 첫 값인 c 가 닫힌 괄호라면 반복문 완전 종료
            # (if 문 안에 있지만, 바로 위에 break 가 있기 때문에 else 가 없어도 됨)
            b = stack.pop() # b = stack 에 저장된 마지막 인덱스 값
            # () 짝 확인하기 위해 가장 마지막 인덱스 값 b로 꺼내 받음
            if not (b == "(" and c == ")"):
                answer = 0
                break
        # print(stack)

    # 반복문 다 끝나고 나서 남은 괄호가 스택에 있는지 검사
    if len(stack) > 0: # 스택 길이가 0보다 크다? 짝 없는 괄호 남아 있다는 뜻
        answer = 0
    print(f'#{tc} {answer}')
'''