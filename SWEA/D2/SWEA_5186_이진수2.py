T = int(input())

for tc in range(1, T + 1):
  N = float(input())
  result = ''

  while N > 0 and len(result) < 13:
    N *= 2
    bit = int(N)
    result += str(bit)
    N -= bit

  if N > 0 or len(result) > 12:
    print(f"{tc} overflow")
  else:
    print(f"{tc} {result}")