T = int(input())

for test_case in range(1, T + 1):

    N, M = map(int, input().split())

    board = []
    result = []

    for _ in range(N):
        board.append(input()) 

    for i in range(N):
        for j in range(N - M + 1):
           word = board[i][j:j + M]

           if word == word[::-1]:
               result.append(word)
    
    for j in range(N):
        for i in range(N - M + 1):
            word = ''
            for k in range(M):
                word += board[i + k][j]
            if word == word[::-1]:
                result.append(word)

    print(f'#{test_case} {result}')