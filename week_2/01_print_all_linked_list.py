class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# node = Node(3)
# first_node = Node(4)
# node.next = first_node
# print(node.next.data)


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            return


        cur = self.head

        while cur.next is not None:
            cur = cur.next
            print("cur is", cur.data)
        cur.next = Node(data)


    def print_all(self):
        print('zzzz')
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next


Linked_list = LinkedList(3)
Linked_list.append(4)
Linked_list.append(5)
Linked_list.print_all()
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        return "index 번째 노드를 반환해보세요!"

linked_list = LinkedList(5)
linked_list.append(12)
linked_list.get_node(0) # -> 5를 들고 있는 노드를 반환해야 합니다!