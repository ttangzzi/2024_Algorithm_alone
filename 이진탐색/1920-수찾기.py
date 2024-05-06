# 버블정렬로 오름차순 -> 이진탐색을 위해서
# 시간초과 이슈

N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

# sorted 함수를 사용하여 시간복잡도 이슈 해결
A = sorted(A)

for key in range(M):
  pl = 0
  pr = len(A)-1
  while True:
    pc = (pl + pr) // 2
    
    # 중앙값과 B에 해당하는 값이 같다면 찾기에 성공했으므로 1을 출력 후 빠져나간다.
    if A[pc] == B[key]:
      print(1)
      break
    
    # 중앙보다 B값이 큰 경우 B값보다 큰 값을 가진 인덱스에서 다시 검색하도록 pl을 조정한다.
    elif A[pc] < B[key]:
      pl = pc + 1
      
    # 중앙보다 B값이 작은 경우 B값보다 작은 값을 가진 인덱스에서 다시 검색하도록 pr을 조정한다.
    else:
      pr = pc - 1
      
    # pl이 pr보다 크다면 리스트에 해당값이 없다 즉, 찾기 실패라고 판단하여 0을 출력 후 빠져나간다.
    if pl > pr:
      print(0)
      break