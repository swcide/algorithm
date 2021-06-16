"""
문제
정수를 저장하는 스택을 구현한 다음,
입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

명령은 총 다섯 가지이다.
"""
"""
push X: 정수 X를 스택에 넣는 연산이다.
pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다.
     약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 스택에 들어있는 정수의 개수를 출력한다.
empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
top: 스택의 가장 위에 있는 정수를 출력한다.
     만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.


예제  1      출력
14          
push 1      
push 2      
top         2
size        2
empty       0
pop         2
pop         1
pop         -1
size        0
empty       1
pop         -1
push 3      
empty       0
top         3

예제  2     출력
7
pop         -1
top         -1
push 123    
top         123
pop         123
top         -1
pop         -1

"""
import time
start_time = time.time()
import sys

input=sys.stdin.readline

n = int(input())
stack = []
ans  =[]
for i in range(n):
    commend =input()
    ans = commend.split()

    if 1<len(ans):
        stack.append(int(ans[1]))


    if ans[0]=="pop":
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())
    if ans[0] =="size":
        print(len(stack))
    if ans[0] == "empty":
        if len(stack) ==0:
            print(1)
        else:
            print(0)
    if ans[0] == "top":
        if len(stack) ==0:
            print(-1)
        else:
            print(stack[-1])



end_time = time.time()
print()
print("시간 측정: {:.10f}".format(end_time - start_time))