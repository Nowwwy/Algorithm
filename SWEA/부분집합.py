# [Set3] 문제2 : 목표 합 부분집합 (백트래킹)
def dfs(idx, cur_sum):
    global count
    # 가지치기: 현재 합이 이미 목표 K를 넘으면 더 이상 진행하지 않음
    if cur_sum > K:
        return
        
    # 목표 K에 도달한 경우
    if cur_sum == K:
        count += 1
        return
        
    # 모든 원소를 다 확인했으면 종료
    if idx == N:
        return
        
    # 1) idx번 원소를 부분집합에 포함
    dfs(idx + 1, cur_sum + nums[idx])
    # 2) idx번 원소를 포함하지 않음
    dfs(idx + 1, cur_sum)


T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    nums = list(map(int, input().split()))
    
    count = 0
    dfs(0, 0)
    print(f"#{tc} {count}")
