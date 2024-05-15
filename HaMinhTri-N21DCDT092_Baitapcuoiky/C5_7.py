class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None

def Chep(cay):
    if cay is None:
        return None
    
    # Sao chép nút hiện tại
    new_node = Node(cay.info)
    
    # Sao chép cây con bên trái và cây con bên phải
    new_node.left = Chep(cay.left)
    new_node.right = Chep(cay.right)
    
    return new_node

# Ví dụ sử dụng:
root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(3)
root.left.right = Node(7)

cay_sao_chep = Chep(root)
# In ra giá trị của cây sao chép để kiểm tra
def DuyetCay(cay):
    if cay:
        DuyetCay(cay.left)
        print(cay.info, end=" ")
        DuyetCay(cay.right)

DuyetCay(cay_sao_chep)
