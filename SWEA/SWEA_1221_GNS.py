T = int(input())

for test_case in range(1, T + 1):
    tc, tclen= input().split()

    text = list(input().split())

    result = []

    num = {
    "ZRO" : 0,
    "ONE" : 1,
    "TWO" : 2,
    "THR" : 3,
    "FOR" : 4,
    "FIV" : 5,
    "SIX" : 6,
    "SVN" : 7,
    "EGT" : 8,
    "NIN" : 9
    }

    words = [
    "ZRO",
    "ONE",
    "TWO",
    "THR",
    "FOR",
    "FIV",
    "SIX",
    "SVN",
    "EGT",
    "NIN"
    ]

    for i in range(int(tclen)):
        result.append(num[text[i]])
    result.sort()

    real_result = ""

    for i in result:
        real_result += words[i] + " "

    print(f'{tc}\n{real_result}')