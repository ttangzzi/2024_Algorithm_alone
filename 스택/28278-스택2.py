# 1 X: 정수 X를 스택에 넣는다. (1 ≤ X ≤ 100,000) push
# 2: 스택에 정수가 있다면 맨 위의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다. pop
# 3: 스택에 들어있는 정수의 개수를 출력한다. len
# 4: 스택이 비어있으면 1, 아니면 0을 출력한다. len = 0 ?
# 5: 스택에 정수가 있다면 맨 위의 정수를 출력한다. 없다면 -1을 대신 출력한다. top
import sys

N = int(sys.stdin.readline())
stack = []

for _ in range(N):
    order = sys.stdin.readline().split()

    if order[0] == '1':
        stack.append(int(order[1]))
    elif order[0] == '2':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
        
    elif order[0] == '3':
        print(len(stack))
    elif order[0] == '4':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif order[0] == '5':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])