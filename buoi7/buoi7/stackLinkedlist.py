class Node:
    def __init__(self ,value = None ):
        self.value = value
        self.next = None
    def __str__(self):
        return str(self.value)    
class LinkedList:
    def __init__(self):
        self.head = None
        
class Stack:
    def __init__(self):
        self.LinkedList = LinkedList()

 
    def isEmpty(self):
        if self.LinkedList.head == None:
            return True
        else:
            return False
    def push(self, value):
          node = Node(value)
          node.next = self.LinkedList.head
          self.LinkedList.head = node
    def pop(self):
        if self.isEmpty():
            return "There is not any element in the stack"
        else:
            nodeValue = self.LinkedList.head.value
            self.LinkedList.head = self.LinkedList.head.next 
            return nodeValue
    def peek(self):
        if self.isEmpty():
            return "There is not any element in the stack"
        else:
            NodeValue = self.LinkedList.head.value
            return NodeValue
    def delete(self):
        self.LinkedList.head = None
customStack = Stack()
customStack.push(2)
customStack.push(3)
customStack.push(1)
print(customStack)
print("--------")
customStack.pop()
print(customStack)
