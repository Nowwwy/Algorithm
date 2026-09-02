T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    fly = []
    max_fly = 0

    ## 파리 모음집 ##
    for _ in range(N):
        fly.append(list(map(int, input().split())))

    ## 파리채 등장## 칸넘어가면 안되니까 빼주고 1더하고 뭔말알?
    for i in range(N - M + 1):
        for j in range(N - M + 1):

            ## 파리채 내부 위치  및 초기화##
            total = 0
            for x in range(M):
                for y in range(M):
                    total += fly[i + x][j + y]

            ## 파리 많이 잡기 ##
            if total > max_fly:
                max_fly = total

    print(f'#{test_case} {max_fly}')