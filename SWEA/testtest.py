T = int(input())

hexa_digits = '0123456789ABCDEF'

for tc in range(1, T + 1):
  N, hexa = input().split()
  result = ''

  for ch in hexa:
    for i in range(len(hexa_digits)):
      if ch == hexa_digits[i]:
        num = i
        break

  bits = ''

  for _ in range(4):
    bits = str(num % 2) + bits
    num //= 2
  result += bits

  print(f'{tc} {result}')