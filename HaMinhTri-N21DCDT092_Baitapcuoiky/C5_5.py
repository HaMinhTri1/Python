class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None

def KiemTraBST(cay, min_val=float('-inf'), max_val=float('inf')):
    if cay is None:
        return True
    
    # Kiểm tra giá trị của nút hiện tại có nằm trong khoảng hợp lệ không
    if cay.info <= min_val or cay.info >= max_val:
        return False
    
    # Kiểm tra BST cho cây con bên trái và cây con bên phải
    return (KiemTraBST(cay.left, min_val, cay.info) and
            KiemTraBST(cay.right, cay.info, max_val))

# Ví dụ sử dụng:
root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(3)
root.left.right = Node(7)

ket_qua = KiemTraBST(root)
if ket_qua:
    print("Cây là cây nhị phân tìm kiếm (BST).")
else:
    print("Cây không phải là cây nhị phân tìm kiếm (BST).")
