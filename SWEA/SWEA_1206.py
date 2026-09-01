T = 10

for test_case in range(1, T + 1):
  N = int(input())

  building = list(map(int, input().split()))

  result = 0

  for i in range(2, N - 2):

    near = building[i - 2]

    if building[i - 1] > near:
        near = building[i - 1]

    if building[i + 1] > near:
        near = building[i + 1]

    if building[i + 2] > near:
        near = building[i + 2]

    if building[i] > near:
        result += building[i] - near

  print(f'#{test_case} {result}')