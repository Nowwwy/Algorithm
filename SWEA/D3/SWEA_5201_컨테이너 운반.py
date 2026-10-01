T = int(input())

for tc in range(1, T + 1):
    N, M = map(int,input().split())

    wi = list(map(int, input().split()))
    ti = list(map(int, input().split()))

    wi.sort(reverse=True)
    ti.sort(reverse=True)

    cnt = 0
    total = 0
    idx = 0
    truck = 0

    while True:
        if idx == N or truck == M:
            break
        if ti[truck] >= wi[idx]:
            total += wi[idx]
            truck += 1
        idx += 1

    print(f'#{tc} {total}')