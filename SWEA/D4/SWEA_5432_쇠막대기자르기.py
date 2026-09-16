def solve(data):
    total_cnt = 0
    cnt = 0 # 레이저에 의해 생기는 쇠막대기 개수
    for i in range(len(data)):
        if data[i] == '(' and data[i+1] != ')':
            cnt += 1
        elif data[i] == ')':
            if data[i-1] == '(':
                total_cnt += cnt
            else:
                cnt -= 1
                total_cnt += 1

    return total_cnt

T = int(input())

for test_case in range(1, T + 1):
    data = input()
    result = solve(data)
    print(f'#{test_case} {result}')