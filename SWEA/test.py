T = int(input())

hexa_digits = '0123456789ABCDEF'

for tc in range(1, T + 1):
  N = int(input())
  char = input()
  result = ''
  cnt = 0
  for ch in char:
    for i in range(len(hexa_digits)):
      if ch == hexa_digits[i]:
        num = i
        break

    bits = ''

    for _ in range(4):
      bits = str(num % 2) + bits
      num //= 2
    result += bits

  for i in range(len(result) - 1):
    if result[i] == '1' and result[i + 1] == '1':
      cnt += 1

  print(f'#{tc} {cnt}')