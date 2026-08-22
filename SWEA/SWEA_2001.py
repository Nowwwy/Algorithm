T = int(input())

for test_case in range(1, T + 1):

  N, M = map(int, input().split())

  matrix = []
  max_flies = 0

  for i in range(N):
    row = list(map(int, input().split()))
    matrix.append(row)

  for i in range(N - M + 1):
    for j in range(N - M + 1):

      total = 0

      for x in range(M):
        for y in range(M):
          total += matrix[i + x][j + y]

      if total > max_flies:
        max_flies = total

  print(f'#{test_case} {max_flies}')