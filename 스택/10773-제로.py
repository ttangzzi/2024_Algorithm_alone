K = int(input())
stack = []
sum = 0
for _ in range(K):
  num = int(input())

  if num != 0:
    stack.append(num)
  else:
    stack.pop()

for i in range(len(stack)):
  sum += stack[i]

print(sum)