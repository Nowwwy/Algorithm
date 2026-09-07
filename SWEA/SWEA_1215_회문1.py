T = 10

for test_case in range(1, T + 1):

  char = input()
  text = input()
  
  for i in range(8):
    for j in range(8 - M + 1):
      word = board[i][j:j + M]

      if word == word[::-1]:
        cnt += 1

  for j in range(8):
    for i in range(8 - M + 1):

      word = ''

      for k in range(M):
        word += board[i + k][j]

      if word == word[::-1]:
        cnt += 1

  print(f'#{test_case} {cnt}')