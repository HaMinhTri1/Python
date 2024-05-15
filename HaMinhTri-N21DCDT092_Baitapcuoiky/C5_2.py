class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None

def ChieuCao(cay):
    if cay is None:
        return 0
    else:
        # Tính chiều cao của cây con bên trái và cây con bên phải
        chieu_cao_trai = ChieuCao(cay.left)
        chieu_cao_phai = ChieuCao(cay.right)
        
        # Trả về chiều cao lớn nhất giữa hai cây con và cộng thêm 1
        return max(chieu_cao_trai, chieu_cao_phai) + 1

# Ví dụ sử dụng:
root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(3)
root.left.right = Node(7)

chieu_cao = ChieuCao(root)
print(f"Chiều cao của cây là: {chieu_cao}")
