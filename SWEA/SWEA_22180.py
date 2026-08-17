N, M = map(int, input().split())

numbers = list(map(int, input().split()))

result = []

for _ in range(M):
  total = 0
  i, j = map(int, input().split())

  for k in range(i, j+1):
    total += numbers[k-1]
  result.append(total)

print(*result, sep="\n")