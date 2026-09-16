T = int(input())

for _ in range(T):
    test_case = int(input())
    scores = list(map(int, input().split()))

    count = [0] * 101

    for score in scores:
        count[score] += 1

    max_count = 0
    answer = 0

    for score in range(101):
        if count[score] >= max_count:
            max_count = count[score]
            answer = score

    print(f'#{test_case} {answer}')