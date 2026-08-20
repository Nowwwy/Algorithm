T = int(input())

for test_case in range(1, T + 1):

    N, M = map(int, input().split())

    Aij = []

    for i in range(N):
        height = list(map(int, input().split()))
        Aij.append(height)

    candidate = 0

    for i in range(N):
        for j in range(M):
            cand = Aij[i][j]    # (i,j) 현재 위치의 높이
            count = 0
            for k in range(8):  # (i,j) 를 감싸는 8칸 보기 
                di = [-1, -1, -1, 0, 0, 1, 1, 1]
                dj = [-1, 0, 1, -1, 1, -1, 0, 1]
                
                ni = i + di[k]
                nj = j + dj[k]

                if 0 <= ni < N and 0 <= nj < M:
                    if cand > Aij[ni][nj]:
                        count += 1
            if count >= 4:
                candidate += 1

    print(f'#{test_case} {candidate}')