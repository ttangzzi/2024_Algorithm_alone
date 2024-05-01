array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
search = 11

pl = 0
pr = len(array)-1

while True:
  pc = (pl + pr) // 2

  if array[pc] == search:
    print("찾았다")
    break
  elif array[pc] > search:
    print(array[pc])
    pr = pc - 1
  else:
    print(array[pc])
    pl = pc + 1
  
  if pl > pr:
    print("못 찾았다")
    break