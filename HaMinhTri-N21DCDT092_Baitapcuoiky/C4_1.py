class Node:
    def __init__(self, value):
        self.Info = value
        self.Next = None

class DSLK:
    def __init__(self):
        self.head = None

    def ThemPhanTu(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.Next:
                current = current.Next
            current.Next = new_node
   # def INnguocDequi(self,node):
        #if Node is None:
            #return 
        #self.INnguocDequi(Node.next)
       # print(Node.Info,end=' ')
    def InNguoc(self):
        print("Danh sách liên kết in ngược (đệ qui):")
        self.INnguocDequi(self.head)
        print()  
    def InNguoc_KhongDeQui(self):
        stack = []
        current = self.head
        while current:
            stack.append(current.Info)
            current = current.Next
        while stack:
            print(stack.pop(), end=" ")
  
# Sử dụng ví dụ
dslk = DSLK()
dslk.ThemPhanTu(1)
dslk.ThemPhanTu(2)
dslk.ThemPhanTu(3)

dslk.InNguoc()

print("\nIn ngược bằng không đệ qui:")
dslk.InNguoc_KhongDeQui()
