# 계산기 1 (중위 표기법을 후위 표기법으로)

# 스택 밖 우선 순위
icp = {"+" : 1, "-" : 1, "/" : 2, "*" : 2, "(" : 3}
# 스택 안 우선 순위
isp = {"+" : 1, "-" : 1, "/" : 2, "*" : 2, "(" : 0}

# infix : 중위 표기식
# n : 식의 길이
def get_postfix(infix, n):
    postfix = ""    # 결과로 출력할 후위 표기식
    stack = []

    # infix 안에 있는 문자들을 하나씩 떼와서 처리
    for i in range(n):
        # 피연산자인 경우
        if "0" <= infix[i] <= "9":
            # 결과에 출력
            postfix += infix[i]
        # 연산자인 경우
        else:
            # 닫는 괄호
            if infix[i] == ")":
                # 여는 괄호가 나올때 까지 pop 해서 결과에 출력
                while stack:
                    char = stack.pop()
                    if char == "(":
                        break
                    postfix += char
            # 다른 연산자 나오는 경우
            else:
                # 현재 토큰(연사자)의 우선순위보다 stack[top]의 우선순위dhk
                # 같거나 높으면 계속 pop
                while stack and isp[stack[-1]] >= icp[infix[i]]:
                    postfix += stack.pop()
                # 아니면 push
                stack.append(infix[i])
    # 남아있는 연산자를 출력
    while stack:
        postfix += stack.pop()
    return postfix
string = "2+3*4/5"
n = len(string)
print(get_postfix(string, n))   # 234*5/+

# 계산기 2 (후위 표기법을 스택으로 계산)
def get_result(postfix):
    stack = []

    for c in postfix:
        # 피연산자 만나면 스택에 넣기
        if "0" <= c <= "9":
            stack.append(int(c))
        # 연산자  만나면 피연산자를 두개 꺼내서 계산
        else:
            # 우항, 오른쪽 먼저
            right = stack.pop()
            # 좌항, 왼쪽이 나중에
            left = stack.pop()

            if c == "+":
                result = left + right
            elif c == "-":
                result = left - right
            elif c == "*":
                result = left * right
            elif c == "/":
               result = left / right

            stack.append(result)

    return stack.pop()
string = "2+3*4/5"
n = len(string)
postfix = get_postfix(string, n)
print(get_result(postfix))  # 4.4