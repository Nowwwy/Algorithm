txt = input()
pair = {')':'(','}':'{'}
top = -1
stack = [0] * 100

ans = 1

for x in txt:
    if x in '{(':
        top += 1
        stack[top] = x
    elif x in ')}':
        if top == -1:
            ans = 0
            break
        else:
            top -= 1
            tmp = stack[top + 1]
            if pair[x] != tmp:
                ans = 0
                break

if top != -1:
    ans = 0

print(ans)