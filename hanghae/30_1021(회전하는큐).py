"""
문제
지민이는 N개의 원소를 포함하고 있는 양방향 순환 큐를 가지고 있다.
지민이는 이 큐에서 몇 개의 원소를 뽑아내려고 한다.

지민이는 이 큐에서 다음과 같은 3가지 연산을 수행할 수 있다.

첫 번째 원소를 뽑아낸다. 이 연산을 수행하면,
원래 큐의 원소가 a1, ..., ak이었던 것이 a2, ..., ak와 같이 된다.
왼쪽으로 한 칸 이동시킨다. 이 연산을 수행하면,
a1, ..., ak가 a2, ..., ak, a1이 된다.
오른쪽으로 한 칸 이동시킨다. 이 연산을 수행하면,
a1, ..., ak가 ak, a1, ..., ak-1이 된다.
큐에 처음에 포함되어 있던 수 N이 주어진다.
그리고 지민이가 뽑아내려고 하는 원소의 위치가 주어진다.
 (이 위치는 가장 처음 큐에서의 위치이다.) 이때, 그 원소를 주어진 순서대로 뽑아내는데 드는 2번, 3번 연산의 최솟값을 출력하는 프로그램을 작성하시오.


"""

"""
예제 입력 1             예제 출력 1 
10 3
1 2 3                       0

예제 입력 2             예제 출력 2 
10 3    
2 9 5                       8

예제 입력 3             예제 출력 3 
32 6    
27 16 30 11 6 23            59

예제 입력 4             예제 출력 4 
10 10
1 6 3 2 7 9 8 4 10 5        14


"""


from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
idxs = list(map(int, input().split()))
dq = deque([i for i in range(1, n+1)])

count = 0
for idx in idxs:
    while True:
        if dq[0] == idx:
            dq.popleft()
            break
        else:
            if dq.index(idx) < len(dq)/2:
                while dq[0] != idx:
                    dq.append(dq.popleft())
                    count += 1
            else:
                while dq[0] != idx:
                    dq.appendleft(dq.pop())
                    count += 1
print(count)


"""
나중에 알아보도록 하자...
"""