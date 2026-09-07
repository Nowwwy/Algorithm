T = int(input())

for test_case in range(1, T + 1):
    char = input()
    text = input()

    high = 0

    for i in range(len(char)):
        cnt = 0
        for j in range(len(text)):
            if char[i] == text[j]:
                cnt += 1

        if cnt > high:
            high = cnt 

    print(f'#{test_case} {high}')