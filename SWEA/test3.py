T = int(input())

hexa_digits = '0123456789ABCDEF'

for tc in range(1, T + 1):
  N = int(input())
  nums = input()
  result = ''
  cnt = 0

  for ch in nums:
    for i in range(16):
      if ch == hexa_digits[i]:
        num = i
        break

    bits = ''

    for _ in range(4):
      bits = str(num % 2) + bits
      num //= 2
    result += bits

  for i in range(len(result)):
    if i % 2 == 0 and result[i] == '1':
      cnt += 2
    elif i % 2 == 1 and result[i] == '1':
      cnt += 1
    else:
      continue

  print(f'#{tc} {cnt}')