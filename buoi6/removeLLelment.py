class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Node:
  def __init__(self, value):
    self.value = value 
    self.next = None        
class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    self.length = 0

  def append(self, value):
    new_node = Node(value)
    if self.head is None:
        self.head = new_node
        self.tail = new_node 
    else:
        self.tail.next = new_node
        self.tail = new_node
    self.length += 1
  def __str__(self):
    temp_node = self.head
    result = ''
    while temp_node is not None:
      result += str(temp_node.value)
      if temp_node.next is not None:
         result += ' -> '
      temp_node = temp_node.next 
    return result
def remove_elements(head, val):
    new_node = Node(-1)
    new_node.next = head
    current = new_node

    # Traverse the linked list
    while current.next:
        if current.next.val == val:
            # Skip the node with the target value
            current.next = current.next.next
        else:
            current = current.next

    return new_node.next

#head = ListNode(1, ListNode(2, ListNode(6, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))))
new_linked_list = LinkedList()
new_linked_list.append(1)
new_linked_list.append(2)
new_linked_list.append(3)
new_linked_list.append(4)
new_linked_list.append(6)
new_linked_list.append(6)
head = new_linked_list
new_head = remove_elements(head, 6)

print(new_linked_list)
# Print the modified linked list
while new_head:
    print(new_head.val, end=" -> ")
    new_head = new_head.next
print("None")