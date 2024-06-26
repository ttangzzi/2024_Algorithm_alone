N = int(input())
end_num = 0
cnt = 0
while(1):
  end_num+=1
  if str(end_num).find('666') != -1:
    cnt += 1
  if cnt == N:
    break
print(end_num)