# 모든 경우의 수 수행해보기
# 특정 시점에서 가능한 경우의 모든수행 해보기

# idx번 정류장에서 충전지를 갈아 끼우는 경우,
# 갈아 끼우지 않는 경우를 모두 수행
# 배터리 잔량과, 교환횟수를 인자로 받아서 처리
def solve(idx, remain, cnt):
    global min_cnt
    # cnt: 중간 교환 횟수
    if cnt >= min_cnt:
        return 

    if idx == data[0]: # 마지막 정류장 도착
        if cnt < min_cnt: # 충전횟수 최소라면 업데이트
            min_cnt = cnt
        return

    # idx번 정류장에서 배터리를 교환하지 않고 다음정류장으로 이동
    if remain > 0: # 배터리 잔량이 남아 있을 경우에만 배터리 갈지않는 경우의 수 수행
        solve(idx + 1, remain -1, cnt)
   
    # idx번에서 배터리를 교환한 경우
    # 배터리 잔량 data[idx]
    solve(idx + 1, data[idx] - 1, cnt + 1) # 다음 정류장 이동

T = int(input())

for tc in range(1, T + 1):
    data = list(map(int, input().split()))
    # N = data[0]
    min_cnt = 100
    # 2번 정류장 부터 배터리 교환 결정하면 됩니다.
    solve(2, data[1]-1, 0)

    print(f'#{tc} {min_cnt}')