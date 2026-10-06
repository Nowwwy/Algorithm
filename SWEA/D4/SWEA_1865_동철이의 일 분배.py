# 직원 한 명당 일 하나 시키기
# 최대값 구하기
# 백트래킹 가능한 조건
# >>> 최대값 : 연산을 하면 할 수록 결과가 작아지면 가능
# >>> 최소값 : 연산을 하면 할 수록 결과가 커지면 가능
# idx 번 직원이 각 업무를 수행했을 때 누적확률 구하기
def solve(idx, rate):
    global max_rate
    # idx번 직원이 어떤 업무를 수행하는지 저장할 필요는 없고
    # 모든 직원이 업무를 수행했을 때, 성공확률만 알면 된다!
    if rate <= max_rate:
        return
    
    if idx == N:
        max_rate = max(max_rate, rate)
        return

    # idx번 직원이 업무를 수행하는 모든 경우 수행
    for i in range(N):
        if check[i] == 0:
            # idx번 직원이 i번 업무 수행
            check[i] = 1 # i번 업무 수행 표시
            solve(idx + 1, rate * data[idx][i])
            check[i] = 0 # i번 업무 수행 표시 해제

T = int(input())

for tc in range(1, T + 1):
    # 각 테스트 케이스는 N 과 N * N 행렬로 이루어짐
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            data[i][j] = data[i][j] / 100
    max_rate = 0
    # 업무 중복 배정을 막기위한 확인배열
    check = [0] * N
    solve(0, 1)
    print(f'#{tc} {max_rate * 100:.6f}')