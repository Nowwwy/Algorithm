T = int(input())

for test_case in range(1, T + 1):
    N = int(input())

    def paper(length):
        if length == 10:
            return 1
        if length == 20:
            return 3

        return paper(length - 10) + 2 * paper(length - 20)

    print(f"#{test_case} {paper(N)}")