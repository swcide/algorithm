from collections import deque

a = [1,2,3,4,5]

deq = deque(a)

print(deq)
print(deq.pop())
print(deq.popleft())