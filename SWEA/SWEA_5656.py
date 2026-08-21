T = int(input())

for test_case in range(1, T + 1):

    N, W, H = map(int, input().split())

    brick_map = []
    min_bricks = [H * W]

    for i in range(H):
        brick = list(map(int, input().split()))
        brick_map.append(brick)


    def bead_attack(col):
        for row in range(H):
            if brick_map[row][col] == 0:
                continue

            explode_brick(row, col)

            gravity_brick()
            break

    def explode_brick(row, col):
        power = brick_map[row][col]
        brick_map[row][col] = 0

        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]
        
        for d in range(4):
            for dist in range(1, power):
                nr = row + dr[d] * dist
                nc = col + dc[d] * dist
        
                if 0 <= nr < H and 0 <= nc < W:
                    if brick_map[nr][nc] != 0:
                        explode_brick(nr, nc)

    def gravity_brick():
        for col in range(W):
            write_row = H -1

            for row in range(H - 1, -1, -1):
                if brick_map[row][col] != 0:
                    brick_map[write_row][col] = brick_map[row][col]
                    write_row -= 1

            while write_row >= 0:
                brick_map[write_row][col] = 0
                write_row -= 1

    def dfs(depth):
        if depth == N:
            count = 0

            for i in range(H):
                for j in range(W):
                    if brick_map[i][j] != 0:
                        count += 1

            if count < min_bricks[0]:
                min_bricks[0] = count

            return

        for col in range(W):
            backup = [row[:] for row in brick_map]

            bead_attack(col)
            dfs(depth + 1)

            for r in range(H):
                brick_map[r] = backup[r][:]

    dfs(0)
    print(f'#{test_case} {min_bricks[0]}')