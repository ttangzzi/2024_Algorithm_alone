N = int(input())
# 3킬로그램 봉지와 5킬로그램 봉지의 최소 갯수로 N킬로그램을 채우기
cnt = 0

while N > 0:
  if N % 5 == 0:
    N -= 5
    cnt += 1
  elif N % 3 == 0:
    N -= 3
    cnt += 1
  elif N % 5 != N:
    N -= 5
    cnt += 1
  elif N %3 != N:
    N -=3
    cnt += 1
  else:
    print(-1)
    exit(0)

print(cnt)
