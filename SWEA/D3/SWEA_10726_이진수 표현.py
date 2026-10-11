T = int(input())

for tc in range(1, T + 1):
  N, M = map(int, input().split())
  bits = ''
  while M > 0:
    bits = str(M % 2) + bits
    M //= 2
  print(bits[-N:])
