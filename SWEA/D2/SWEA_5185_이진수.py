T = int(input())

for tc in range(1, T + 1):
  N, hexa = input().split()

  decimal = int(hexa, 16)
  binary = bin(decimal)
  result = binary[2:].zfill(int(N) * 4)

  print(f'#{tc} {result}')


# T = int(input())

# hex_digits = '0123456789ABCDEF'

# for tc in range(1, T + 1):
#     N, hexa = input().split()
#     result = ''

#     for ch in hexa:
#         for i in range(16):
#             if ch == hex_digits[i]:
#                 num = i
#                 break

#         bits = ''

#         for _ in range(4):
#             bits = str(num % 2) + bits
#             num //= 2

#         result += bits

#     print(f'#{tc} {result}')