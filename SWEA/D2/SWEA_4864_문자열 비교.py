T = int(input())

for test_case in range(1, 1 + T):
  char = input()
  sentence = input()
  result = 0

  for i in range(len(sentence) - len(char) + 1):
    if sentence[i:i+len(char)] == char:
      result = 1

  print(f'#{test_case} {result}')