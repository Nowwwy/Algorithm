T = int(input())

for test_case in range(1, T + 1):

  lst = []
  result = 1

  text = input()

  for char in text:
    if char == '(' or char == '{':
      lst.append(char)

    if char == '}':
      if not lst:
        result = 0
      if lst[-1] != '{':
        result = 0
      else:
        lst.pop()

  print(f'#{test_case} {result}')