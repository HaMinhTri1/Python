class Node:
    def __init__(self, heso, somu):
        self.HeSo = heso
        self.SoMu = somu
        self.KeTiep = None

class DaThuc:
    def __init__(self):
        self.head = None

    def Them(self, heso, somu):
        new_node = Node(heso, somu)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.KeTiep:
                current = current.KeTiep
            current.KeTiep = new_node

dathuc = DaThuc()
dathuc.Them(2.5, 3)  # Thêm số hạng 2.5x^3
dathuc.Them(-1.2, 2)  # Thêm số hạng -1.2x^2
dathuc.Them(0.8, 1)  # Thêm số hạng 0.8x
