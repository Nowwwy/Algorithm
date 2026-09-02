T = int(input())

for test_case in range(1, T + 1):
    N = int(input())

    ## 보드판 ##
    board = [[0] * 10 for _ in range(10)]

    ## red blue 색칠할 자리 정하기##
    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())

    ## red blue 색칠하기 ##
        for i in range(r1, r2 + 1):
            for j in range(c1, c2 + 1):
                board[i][j] += color

    ## red blue 합치면 purple ##
    purple = 0

    ## purple 갯수 찾기 red + blue = 3 purple은 3임 ##
    for i in range(10):
        for j in range(10):
            if board[i][j] == 3:
                purple += 1

    print(f'#{test_case} {purple}')