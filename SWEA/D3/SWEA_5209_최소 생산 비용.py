def solve(idx, check, sum_v):
    global min_v

    # 현재까지의 비용이 이미 최소 비용보다 크다면
    # 더 탐색할 필요가 없으므로 가지치기
    if sum_v >= min_v:
        return

    # 모든 제품의 생산 공장을 결정했다면
    if idx == N:
        # 지금까지의 최소 생산 비용 갱신
        min_v = min(min_v, sum_v)
        return

    # idx번째 제품을 생산할 공장 선택
    for i in range(N):

        # 아직 사용하지 않은 공장이라면
        if check[i] == 0:

            # i번 공장 사용 처리
            check[i] = 1

            # 다음 제품으로 이동
            # 현재 제품의 생산 비용 factory[idx][i]를 누적
            solve(idx + 1, check, sum_v + factory[idx][i])

            # 다른 경우의 수도 확인하기 위해
            # i번 공장을 다시 사용 가능 상태로 복구 (백트래킹)
            check[i] = 0


T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    # 생산 비용 입력
    # factory[idx][i] : idx번째 제품을 i번 공장에서 생산하는 비용
    factory = [list(map(int, input().split())) for _ in range(N)]

    # 현재까지 찾은 최소 생산 비용
    min_v = 99999999

    # 0번째 제품부터 탐색 시작
    # check[i] : i번 공장 사용 여부
    # sum_v : 현재까지의 생산 비용
    solve(0, [0] * N, 0)

    print(f'#{tc} {min_v}')