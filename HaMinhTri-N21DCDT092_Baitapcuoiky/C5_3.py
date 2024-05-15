class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
def SoNutLa(cay):
    if cay is None:
        return 0
    elif cay.left is None and cay.right is None:
        # Nếu nút là không có cây con bên trái và bên phải, đó là nút lá
        return 1
    else:
        # Đệ quy tính số nút lá của cây con bên trái và cây con bên phải
        so_nut_la_trai = SoNutLa(cay.left)
        so_nut_la_phai = SoNutLa(cay.right)    
        # Tổng số nút lá của cây gốc
        return so_nut_la_trai + so_nut_la_phai
root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(3)
root.left.right = Node(7)
root.right.right = Node(10)
root.right.left = Node(10)
so_nut_la = SoNutLa(root)
print(f"Số nút lá của cây là: {so_nut_la}")
