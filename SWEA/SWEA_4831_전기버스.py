T = int(input())

for test_case in range(1, T + 1):
    K, N ,M = map(int, input().split())
    charger = list(map(int, input().split()))

    result = 0
    current = 0

    for i in range(N):

        if current + K >= N:
            break

        next_charger = current

        for j in range(M):
            if current < charger[j] <= current + K:
                if charger[j] > next_charger:
                    next_charger = charger[j]

        if next_charger == current:
            result = 0
            break

        current = next_charger
        result += 1
    print(f'#{test_case} {result}')