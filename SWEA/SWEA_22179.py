N, M = map(int, input().split())

arr = []

for i in range(N):
  row = list(map(int, input().split()))
  arr.append(row)

for j in range(M):
  for i in range(N - 1, -1,-1):
    print(arr[i][j], end=' ')
  print()