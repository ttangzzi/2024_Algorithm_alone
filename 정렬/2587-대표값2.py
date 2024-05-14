import sys

N = [int(sys.stdin.readline()) for _ in range(5)]
sum = 0
N.sort()

for i in range(len(N)):
  sum += N[i]
print(int(sum / len(N)))
print(N[2])