T = int(input())

for tc in range(1, T + 1):
  N, M = map(int, input().split())
  bits = ''
  while M > 0:
    bits = str(M % 2) + bits
    M //= 2
  if bits[-N:] == '1' * N:
    print(f'#{tc} ON')
  else:
    print(f'#{tc} OFF')