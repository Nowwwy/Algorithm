T = int(input())

for test_case in range(1, T + 1):
    K, N ,M = map(int, input().split())
    charger = list(map(int, input().split()))

    result = 0
    current = 0

    
    while current + K < N:
        next_charger = current

        for i in range(M):
            if current < charger[i] <= current + K:
                if charger[i] > next_charger:
                    next_charger = charger[i]

        if next_charger == current:
                result = 0
                break

        current = next_charger
        result += 1

    print(f'#{test_case} {result}')