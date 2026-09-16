T = int(input())

for test_case in range(1, T + 1):
  N, M = map(int, input().split())
  numbers = list(map(int, input().split()))

  for i in range(N - M + 1):
    total = 0

    for j in range(M):
      total += numbers[i + j]

    if i == 0:
      high = total
      low = total
    else:
      if total > high:
        high = total
      if total < low:
        low = total

  print(f'#{test_case} {high - low}')