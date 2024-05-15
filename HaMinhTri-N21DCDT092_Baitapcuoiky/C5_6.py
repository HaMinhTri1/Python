class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None

def ChieuCao(cay):
    if cay is None:
        return 0
    else:
        chieu_cao_trai = ChieuCao(cay.left)
        chieu_cao_phai = ChieuCao(cay.right)
        return max(chieu_cao_trai, chieu_cao_phai) + 1

def KiemTraAVL(cay):
    if cay is None:
        return True
    
    chieu_cao_trai = ChieuCao(cay.left)
    chieu_cao_phai = ChieuCao(cay.right)

    if abs(chieu_cao_trai - chieu_cao_phai) <= 1:
        return KiemTraAVL(cay.left) and KiemTraAVL(cay.right)
    else:
        return False

# Ví dụ sử dụng:
root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(3)
root.left.right = Node(7)
root.left.left.left = Node(9)
ket_qua = KiemTraAVL(root)
if ket_qua:
    print("Cây là cây nhị phân cân bằng (AVL).")
else:
    print("Cây không phải là cây nhị phân cân bằng (AVL).")
