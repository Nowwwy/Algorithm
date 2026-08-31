T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))

    high = max(numbers)
    low = min(numbers)

    result = high - low

    print(f'#{test_case} {result}')