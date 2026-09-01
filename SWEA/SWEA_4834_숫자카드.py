T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    cards = list(map(int, input()))

    cnt = [0] * 10
    for i in range(N):
        num = cards[i]
        cnt[num] += 1

    max_card = 0
    max_card_cnt = 0
    for j in range(len(cnt)):
        if cnt[j] >= max_card_cnt:
            max_card_cnt = cnt[j]
            max_card = j

    print(f'{test_case} {max_card} {max_card_cnt}')