def solve():



T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))

    pairs = [[] for _ in range(N + 1)]

    for i in range(0, len(nums), M):
        start = nums[i]
        end = nums[i + 1]
        pairs[start].append(end)
    print(pairs)