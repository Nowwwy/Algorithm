for test_case in range(1, 11):
  N = int(input())

  magnetic = []

  for _ in range(N):
    row = list(map(int, input().split()))
    magnetic.append(row)

  count = 0

  for col in range(N):
    state = 0

    for row in range(N):
      pole = magnetic[row][col]

      if pole == 1:
        state = 1

      if pole == 2 and state == 1:
        count += 1
        state = 0
        
  print(f'#{test_case} {count}')