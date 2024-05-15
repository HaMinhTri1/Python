class Node:
    def __init__(self, info):
        self.info = info
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def InNguocRecursion(self, node):
        if node is None:
            return
        self.InNguocRecursion(node.next)
        print(node.info, end=" ")

    def InNguoc(self):
        print("Danh sách liên kết in ngược (đệ qui):")
        self.InNguocRecursion(self.head)
        print()
    def InNguocStack(self):
        stack = []
        current = self.head
        while current:
            stack.append(current.info)
            current = current.next
        print("Danh sách liên kết in ngược (không đệ qui):")
        while stack:
            print(stack.pop(), end=" ")
# Ví dụ sử dụng:
dslk = LinkedList()
dslk.head = Node(1)
second = Node(2)
third = Node(3)
dslk.head.next = second
second.next = third
dslk.InNguoc()
dslk.InNguocStack()