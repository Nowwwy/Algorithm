N = int(input())

numbers = list(map(int, input().split()))

high = max(numbers)
low = min(numbers)

print(high, low)