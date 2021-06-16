"""
스택 이라는 자료 구조에서 제공하는 기능은 다음과 같습니다!

**push(data)** : 맨 앞에 데이터 넣기
**pop()** : 맨 앞의 데이터 뽑기
**peek()** : 맨 앞의 데이터 보기
**isEmpty()**: 스택이 비었는지 안 비었는지 여부 반환해주기

한 번, 직접 구현해볼까요?

그 전에! 과연 스택은 뭘로 구현하면 좋을까요?
**데이터 넣고 뽑는 걸 자주하는** 자료 구조입니다!

어, 우리 같이 배웠죠! 그렇습니다. 링크드 리스트와 유사하게 구현할 수 있습니다!
아래 코드를 기반으로 한 번 같이 구현해보겠습니다!


"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        new_head = Node(value)
        new_head.next = self.head
        self.head = new_head

    # pop 기능 구현
    def pop(self):
        if self.is_empty():
            return "Stack is Empty"

        delete_head = self.head
        self.head = self.head.next

        return delete_head

    def peek(self):
        if self.is_empty():
            return "Stack is Empty"

        return self.head.data

    # isEmpty 기능 구현
    def is_empty(self):
        return self.head is None

stack = Stack()
stack.push(3)
print(stack.peek())
stack.push(4)
print(stack.peek())
print(stack.pop().data)
print(stack.peek())
print(stack.is_empty())
print(stack.pop)
print(stack.is_empty())

"""
실전에선 리스트로 구현 가능.
스택이 어떤 구조로 실행되는지 알아보았습니다!
"""

"""
push 리스트의 가장 마지막에 원소를 넣는다
pop  리스트의 가장 마지막 원소를 제거하고 값을 리턴해 가져온다. 
top(peek) 가장 마지막 원소를 제거하지 않고 가져온다. list[-1]
"""