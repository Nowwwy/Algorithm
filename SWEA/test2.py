T = int(input())

hexa_digits = '0123456789ABCDEF'

for tc in range(1, T + 1):
  N = int(input())
  nums = input()

  result = ''
  cnt = 0
  max_cnt = 0
  for ch in nums:
    for i in range(16):
      if ch == hexa_digits[i]:
        num = i
        break

    bits = ''

    for _ in range(4):
      bits = str(num % 2) + bits
      num //= 2
  
    reversed_bits = ''
    for i in bits:
      if i == '0':
        reversed_bits += '1'
      else:
        reversed_bits += '0'
    result += reversed_bits

  for i in range(len(result)):
    if result[i] == '1':
      cnt += 1
    else:
      cnt = 0
    max_cnt = max(max_cnt, cnt)
  print(result)
  print(f'#{tc} {max_cnt}')