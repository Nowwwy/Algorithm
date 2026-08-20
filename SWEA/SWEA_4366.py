T = int(input())

for test_case in range(1, T + 1):
    binary = list(input())
    ternary = list(input())

    b = []
    t = []

    for i in range(len(binary)):
        bibox = binary[i]
        for j in range(2):
            if bibox != str(j):
                binary[i] = str(j)

                chbinary = int(''.join(binary), 2)
                b.append(chbinary)
                binary[i] = bibox

    for i in range(len(ternary)):
        terbox = ternary[i]

        for j in range(3):
            if terbox != str(j):
                ternary[i] = str(j)

                chternary = int(''.join(ternary), 3)
                t.append(chternary)
                ternary[i] = terbox

    for num in b:
        if num in t:
            print(f'#{test_case} {num}')