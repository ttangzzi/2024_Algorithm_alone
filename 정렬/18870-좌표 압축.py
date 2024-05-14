import sys
N = int(sys.stdin.readline())
X = list(map(int,(sys.stdin.readline().split())))
dic = {}

X_j = list(set(X)) # 중복 제거 => set
X_j.sort() # 정렬하기 => sort

# 오름차순으로 value를 매핑
for i in range(len(X_j)): 
  dic[X_j[i]] = i

# 원본 기준으로 key에 맞는 value를 출력한다.
for i in range(len(X)):
  print(dic[X[i]], end=" ")