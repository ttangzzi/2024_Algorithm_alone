N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

for i in range(N-1):
  for j in range(N-1, i, -1):
    if A[j - 1] > A[j]:
      A[j - 1], A[j] = A[j], A[j-1]

pl = 0
pr = N-1
key = 0

while True:
  pc = (pl + pr) // 2
  if A[pc] == B[key]:
    print(1)
  elif A[pc] < B[key]:
    pl = pc + 1
  else:
    pr = pc-1
  if pl > pr:
    print(0)
    break
  key += 1

