N = int(input())

numbers = list(map(int, input().split()))

total = sum(numbers)
avg = total // N
print(total, avg)