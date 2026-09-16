N = int(input())

words = []

for i in range(N):
  word = input()
  words.append(word)

for word in words:
  print(word[::-1])