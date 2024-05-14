# import sys

# N = int(sys.stdin.readline())
# NList = [0] * N
# stack = []
# NListTurn = 0
# pop = 0

# for i in range(N):
#     NList[i] = int(sys.stdin.readline())

# if NList[0] == 1:
#     print("NO")
    
# else :
#     for i in range(1,N+1):
#         stack.append(i)


#         print("+", end="\n")

#         stackTurn = i-1-pop

#         while stack[stackTurn] == NList[NListTurn]:
#             stack.pop()
#             pop += 1
#             print("-", end="\n")
#             if len(stack) == 0:
#                 break
#             else:
#                 stackTurn -= 1
#                 NListTurn += 1

# 1874번 스택 수열
n = int(input())
stack, ans, find = [], [], True
# 숫자 1부터 시작
now = 1
for _ in range(n):
    num = int(input())
    # 스택 쌓기 Push
    while now <= num:
        stack.append(now)
        ans.append('+')
        now += 1
    # 스택 꺼내기 Pop
    if stack[-1] == num:
        stack.pop()
        ans.append('-')
    # 불가능한 경우
    else:
        find = False

# 정답 출력
if not find: # 불가능하다면
    print('NO')
else:
    for i in ans: # 가능하다면
        print(i)

# 출처 : https://data-flower.tistory.com/98