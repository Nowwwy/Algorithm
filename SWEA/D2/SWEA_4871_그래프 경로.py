T = int(input())

for test_case in range(1, T + 1):
  V, E = map(int, input().split())

  graph = [[] for _ in range(V + 1)]

  for _ in range(E):
    start, end = map(int, input().split())
    graph[start].append(end)

  S, G = map(int, input().split())