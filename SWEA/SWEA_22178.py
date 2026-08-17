N, K = map(int, input().split())
numbers = list(map(int, input().split()))

high = 0

for i in range(N - K + 1):
  num = 0

  for j in range(K):
    num += numbers[i + j]

  if num > high:
    high = num

print(high)