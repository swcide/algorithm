"""
정수를 저장하는 큐를 구현한 다음,
입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

명령은 총 여섯 가지이다.

push X: 정수 X를 큐에 넣는 연산이다.
pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다.
     만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 큐에 들어있는 정수의 개수를 출력한다.
empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
front: 큐의 가장 앞에 있는 정수를 출력한다.
       만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 큐의 가장 뒤에 있는 정수를 출력한다.
      만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.


"""


"""
예제  1        출력 
15
push 1
push 2
front          1
back           2 
size           2 
empty          0
pop            1
pop            2
pop            -1
size           0
empty          1
pop            -1
push 3          
empty          0
front          3 


"""


from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
deq = deque()

for i in range(n):
    commend = input().split()

    check = commend[0]

    if len(commend)>1:
        deq.append(commend[1])
    if deq:
        if check=="front":
            print(deq[0])
        elif check =="back":
            print(deq[len(deq)-1])
        elif check =="pop":
            print(deq.popleft())
        elif check =="size":
            print(len(deq))
        elif check =="empty":
            print(0)
    else:
        if check == "front":
            print(-1)
        elif check == "back":
            print(-1)
        elif check == "pop":
            print(-1)
        elif check == "size":
            print(0)
        elif check == "empty":
            print(1)

"""
시간이 많이 걸린다.
나중에 링크드리스트를 구현해서 한번 해본뒤
두 시간을 비교해도  
재밌을 것 같다

"""