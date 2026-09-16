T = int(input())

for test_case in range(1, T + 1):
  N = int(input())

  tri = []

  for i in range(1, N+1):
    tri.append([0] * i)

  for i in range(N):
    tri[i][0] = 1
    tri[i][-1] = 1

  for i in range(1, N):
    for j in range(1, i):
      tri[i][j] = tri[i -1][j -1] + tri[i - 1][j]

  print(f'#{test_case}')

  for row in tri:
    print(*row)