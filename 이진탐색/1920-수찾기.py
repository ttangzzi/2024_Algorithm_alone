# 버블정렬로 오름차순 -> 이진탐색을 위해서
# 시간초과 이슈

N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

# 따라서 sorted 함수를 사용하여 시간복잡도 이슈 해결
A = sorted(A)

for key in range(M):
  pl = 0
  pr = len(A)-1
  while True:
    pc = (pl + pr) // 2
    if A[pc] == B[key]:
      print(1)
      break
    elif A[pc] < B[key]:
      pl = pc + 1
    else:
      pr = pc - 1
    if pl > pr:
      print(0)
      break