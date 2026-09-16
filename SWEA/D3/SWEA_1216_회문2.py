T = 10

for test_case in range(1, T + 1):
  tc = int(input())

  board = []

  for _ in range(100):
    board.append(input())

  answer = 0

  for length in range(100, 0 , -1):
    found = False

    for i in range(100):
      for j in range(100 - length + 1):

        word = board[i][j:j + length]

        if word == word[::-1]:
          answer = length
          found = True
          break

      if found:
        break
    if found:
      break

    for i in range(100):
      for j in range(100 - length + 1):
        word = ''

        for k in range(length):
          word += board[j + k][i]

        if word == word[::-1]:
          answer = length
          found = True
          break

      if found:
        break
    if found:
      break

  print(f'#{tc} {answer}')