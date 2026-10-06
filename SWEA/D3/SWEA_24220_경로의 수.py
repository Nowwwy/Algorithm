# 지금은 공부하시고
# 살아서 공부하시고

# 하기위해서 하지 않는다. 
# 할 말은 많지만 참겠다....

# v번 정점에서 갈 수 있는 길 가기
def dfs(v):
    global cnt, visited
    if v == G:
        # cnt += 1
        cnt = cnt + 1
        return 
    # line[v] : v번에서 갈 수 있는 정점 목록
    
    
    # a = 5 #할당하지 않으면 지역변수를 선언하는게 아니라 글로벌 변수를 사용한다!
    for next_node in line[v]:
        # 방문 체크
        if not visited[next_node]:
            visited[next_node] = 1
            #방문전에 visited로 방문 안하도록 만들기
            dfs(next_node)
            visited[next_node] = 0


T = int(input())

for tc in range(1, T + 1):
    N, E = map(int, input().split())
    Es = list(map(int, input().split()))
    S, G = map(int, input().split())

    line = [[] for _ in range(N + 1)]
    a = 10
    for i in range(0, len(Es), 2):
        start = Es[i]
        end = Es[i+1]
        line[start].append(end)

    cnt = 0
    visited = [0] * (N + 1)
    dfs(S)
    print(f'#{tc} {cnt}')
