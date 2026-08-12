T = int(input())

for test_case in range(1, T + 1):

  board = [list(map(int, input().split())) for _ in range(9)]
  answer = 1

  for i in range(9):
    if len(set(board[i])) != 9:
      answer = 0
  for j in range(9):
    if len(set(board[r][j] for r in range(9))) != 9:
        answer = 0
  for i in range(0, 9, 3):
    for j in range(0, 9, 3):
      numbers = []
      for k in range(i, i + 3):
        for m in range(j, j + 3):
          numbers.append(board[k][m])
      if len(set(numbers)) != 9:
        answer = 0
  print(f'#{test_case} {answer}')