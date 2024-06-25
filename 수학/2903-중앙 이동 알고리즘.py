line = 2
N = int(input())

for i in range(1,N+1):
  line = line + 2**(i-1)
  result = line**2
print(result)