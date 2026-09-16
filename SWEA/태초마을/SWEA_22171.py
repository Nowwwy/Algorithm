N = int(input())

numbers = list(map(int, input().split()))

counts = {}

for num in numbers:
  if num in counts:
    counts[num] = counts[num] + 1
  else:
    counts[num] = 1

for num in sorted(counts):
  print(num, counts[num])