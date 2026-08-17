N, M = map(int, input().split())

total = 0

for i in range(N):
  numbers = list(map(int, input().split()))

  for number in numbers:
    total += number

print(total)