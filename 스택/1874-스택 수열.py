n = int(input())
numList = [0]*n
save = 1

for i in range(n):
  numList[i] = int(input())

for i in range(n):
  count = 1
  while True:

    if count-1 == numList[i]:
      print("-")
      break

    elif count == save+1:
      print("+")
      save = count
      count += 1
    