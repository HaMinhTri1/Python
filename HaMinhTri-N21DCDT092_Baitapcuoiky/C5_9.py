class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None

def CayCon(cay1, cay2):
    if cay1 is None and cay2 is None:
        return True
    elif cay1 is None or cay2 is None:
        return False
    else:
        # Kiểm tra giá trị của nút hiện tại
        if cay1.info == cay2.info:
            return True
        
        # Kiểm tra cây con bên trái và cây con bên phải
        return CayCon(cay1.left, cay2.left) and CayCon(cay1.right, cay2.right)

# Ví dụ sử dụng:
root1 = Node(2)
root1.left = Node(10)
root1.left.left = Node(5)
root1.left.right = Node(15)


root2 = Node(10)
root2.left = Node(5)
root2.right = Node(15)

ket_qua = CayCon(root1, root2)
if ket_qua:
    print("Cây 2 là cây con của cây 1.")
else:
    print("Cây 2 không là cây con của cây 1.")
