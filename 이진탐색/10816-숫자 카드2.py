N = int(input()) # 가지고 있는 숫자 카드의 갯수
A = list(map(int, input().split())) # 숫자 카드에 적힌 정수
M = int(input())
B = list(map(int, input().split())) # 몇 개 가지고있는 숫자 카드인지 구해야 할 M개의 정수
A.sort() # 정렬
# 이진 탐색

for i in range(M):
  count = 0
  save = 0
  pl = 0
  pr = len(A)-1
  while True:
    pc = (pl + pr) // 2

    if A[pc] == B[i]:
      count += 1

    if save == 0:
      if A[pc] < B[i]:
        pl = pc+1
      else:
        pr = pc-1
      if pl > pr: # 왼쪽 모두 순회 시 오른쪽 탐색하러 가기
        save = 1
        pl = 0
        pr = len(A)-1
    
    else:
      if A[pc] <= B[i]:
        pl = pc+1
      else:
        pr = pc-1
      if pl > pr: # 모두 순회 시 종료
        break
        
  if count == 0:
    print(count, end=" ")
  else:
    print(count-1, end=" ")