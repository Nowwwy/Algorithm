T = 10

for test_case in range(1, T + 1):

  N, password = input().split()

  pwd = []

  for i in password:
    if pwd and pwd[-1] == i:
      pwd.pop()

    else:
      pwd.append(i)

  print(f'#{test_case} {"".join(pwd)}')