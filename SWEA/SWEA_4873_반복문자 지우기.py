T = int(input())

for test_case in range(1, T + 1):

    text = list(input())
    top = -1
    stack = []

    for i in range(len(text)):
        if text[i] not in stack:
            stack.append()
            top += 1

        elif text[i] in stack:
            if stack[i] == stack[top]:
                stack.pop()
                stack.pop()
                top -= 2

    result = len(stack)

    print(f'#{test_case} {result}')