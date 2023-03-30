# 괄호검사
import sys
sys.stdin = open('../input.txt', 'r')
'''
t = int(input())
for tc in range(1, t+1):
    code = input()
    stack = []
    # 짝 맞으면 1 출력
    result = 1

    for c in code:
        # code 의 값이 열린 괄호라면, stack 에 추가
        if c == '(' or c == '{':
            stack.append(c)
        # code 의 값이 닫힌 괄호라면
        if c == ')' or c == '}':
            # 첫 인덱스면 0 출력하고 반복문 바로 종료
            if len(stack) == 0:
                result = 0
                break
            # 닫힌 괄호가 첫 인덱스 아니라면, b 에 스택 pop 한 값 저장
            b = stack.pop()

            if not ((b == '(' and c == ')') or (b == '{' and c == '}')):
                result = 0
                # (} {) 같은 값이면 바로 종료
                break
    # 반복문 끝난 뒤에 stack 길이 검사 / 남은 값 있으면 짝 안맞는 것.
    if len(stack) > 0:
        result = 0
    print(f'#{tc} {result}')
'''
# 반복문자 지우기

# 반복문자 생기면 지우고, 앞뒤 연결
# 남은 문자열 길이 출력
# 남은 문자열 없다면 0 출력

# 승현 풀이
t = int(input())
for tc in range(1, t + 1):
    text = input()
    stack = []

    for i in text:
        # 스택 길이가 0 보다 크다면
        if len(stack) > 0:
            # 스택의 마지막 값 pop 해서 b 에 저장
            b = stack.pop()
            # 인덱스 값이 b 와 다르다면
            if i != b:
                # 스택에 b 와 인덱스 값 저장
                stack.append(b)
                stack.append(i)
        # 스택 길이가 0 이라면, 스택에 인덱스 값 저장
        else:
            stack.append(i)
    print(f'#{tc} {len(stack)}')
# Ex) ABCCB
# 1. 스택에 A 저장
# 2. AB 저장
# 3. ABC 저장
# 4. AB 저장 (CC 같으므로 pop 돼서 사라짐)
# 5. A 저장 (BB 같으므로 pop 돼서 사라짐)

# 교수님 풀이
t = int(input())
for tc in range(1, t + 1):
    text = input()
    # 스택 초기화
    size = 1000
    top = -1
    stack = [0] * size

    # 첫 글자(text[0])는 비교 대상 없으니까 일단 스택에 넣기
    top += 1   # 인덱스 값을 0으로 맞춰줌
    stack[top] = text[0]

    # 현재 스택의 꼭대기(top)를 확인해서
    # 현재 글자와 다르면 push
    # 같으면 pop
    for i in range(1, len(text)):   # 스택 2번째부터 보기
        # 스택 꼭대기 값이랑 같은지 확인
        # top = 1 & len(stack) = 0 같은 의미
        if top != -1 and stack[top] == text[i]:
            # top = -1 이면, 꺼내올 원소 없음
            # 꺼낼 수 있는 원소가 있다면 pop
            top -= 1  # pop
        else:
            top += 1
            stack[top] = text[i]  # push
    # 안겹친다면 +1 해서 출력
    print(f"#{tc} {top + 1}")
# Ex) CCA
# 1. 첫 글자 C 스택에 넣기
# 2. 다음 글자 C, 기존 스택에 있던 C랑 text[0] 이랑 겹침
# 3. top 에서 -1 을 빼준다 = pop 해준다
# 4. 안겹친다면? top 에 +1 (text[i] 하나 더 쌓기)