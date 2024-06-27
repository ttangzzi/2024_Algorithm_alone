import sys

N, M = map(int, sys.stdin.readline().split())
S = []
test = []
count = 0

for _ in range(N):
  S.append(sys.stdin.readline())

for _ in range(M):
  test.append(sys.stdin.readline())

set_S = set(S)
print(len(set_S.intersection(list)))