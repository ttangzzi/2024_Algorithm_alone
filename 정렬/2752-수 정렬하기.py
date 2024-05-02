# 사용한 정렬 : 버블정렬
# 버블정렬은 n제곱이기때문에 sorted 쓰는것을 권장함

N = int(input())
A = [0]*N
for i in range(N):
  A[i] = int(input())

for i in range(N-1):
  for j in range(N-1, i, -1):
    if A[j-1] > A[j]:
      A[j-1], A[j] = A[j], A[j-1]

for i in range(N):
  print(A[i])