T = 10

for test_case in range(1, 1 + T):
  tc = int(input())
  char = input()
  sentence = input()

  cnt = 0

  for i in range(len(sentence) - len(char) + 1):
    if sentence[i:i+len(char)] == char:
      cnt += 1

  print(f'#{tc} {cnt}')