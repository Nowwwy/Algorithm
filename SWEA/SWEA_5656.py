T = int(input())

for test_case in range(1, T + 1):

    N, W, H = map(int, input().split())

    brick_map = []

    for i in range(H):
        brick = list(map(int, input().split()))
        brick_map.append(brick)


    def bead_attack(col):
        for row in range(H):
            if brick_map[row][col] == 0:
                continue

            power = brick_map[row][col]

            dr = [-1, 1, 0, 0]
            dc = [0, 0, -1, 1]

            for d in range(4):
                for dist in range(1, power):
                    nr = row + dr[d] * dist
                    nc = col + dc[d] * dist

                    if 0 <= nr < H and 0 <= nc < W:
                        brick_map[nr][nc] == 0
            break