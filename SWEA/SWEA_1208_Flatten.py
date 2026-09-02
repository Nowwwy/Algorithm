T = 10

for test_case in range(1, T + 1):
  dump = int(input())
  box = list(map(int, input().split()))

for _ in range(dump):
  high = 0
  low = 0

  for i in range(1, len(box)):

    if box[i] > box[high]:
      high = i

    if box[i] < box[low]:
      low = i

  box[high] -= 1
  box[low] += 1

  high = 0
  low = 0
    
  for i in range(1, len(box)):
    if box[i] > box[high]:
      high = i

    if box[i] < box[low]:
      low = i

  result = box[high] - box[low]

  print(f'#{test_case} {result}')