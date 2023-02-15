# Forth

def get_result(postfix)
    stack = []

    for c in postfix:
        if "0" <= c <= "9":
            stack.append(int(c))




t = int(input())
for tc in range(1, t+1):
    ls = input().split()


postfix = ls[:-1]

print(f'#{tc} {}')