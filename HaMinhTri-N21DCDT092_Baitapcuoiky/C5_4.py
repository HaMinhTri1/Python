class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None

def SoNutTrungGian(cay):
    if cay is None:
        return 0
    elif ((cay.left is not None) or (cay.right is not None)):
        # Nếu nút có ít nhất một cây con bên trái hoặc bên phải, đó là nút trung gian
         return 1 +  SoNutTrungGian(cay.left) + SoNutTrungGian(cay.right) 
    else:
        # Nếu không, đó không phải nút trung gian
        return 0

# Ví dụ sử dụng:
root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(3)
root.right.left = Node(3)



so_nut_trung_gian = SoNutTrungGian(root)
print(f"Số nút trung gian của cây là: {so_nut_trung_gian - 1 }")
