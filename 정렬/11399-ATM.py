N = int(input())
P = list(map(int, input().split()))

P = sorted(P)
sum = 0

for i in range(N):
  for j in range(i+1):
    sum += P[j]
print(sum)