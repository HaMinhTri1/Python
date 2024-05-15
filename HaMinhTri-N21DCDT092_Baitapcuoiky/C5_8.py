class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def SoSanh(cay1, cay2):
    if cay1 is None and cay2 is None:
        return True
    elif cay1 is None or cay2 is None:
        return False
    else:
        if cay1.data != cay2.data:
            return False
        return SoSanh(cay1.left, cay2.left) and SoSanh(cay1.right, cay2.right)

# Ví dụ sử dụng:
root1 = Node(10)
root1.left = Node(5)
root1.right = Node(15)

root2 = Node(10)
root2.left = Node(9)
root2.right = Node(15)

ket_qua = SoSanh(root1, root2)
if ket_qua:
    print("Hai cây giống nhau.")
else:
    print("Hai cây khác nhau.")
