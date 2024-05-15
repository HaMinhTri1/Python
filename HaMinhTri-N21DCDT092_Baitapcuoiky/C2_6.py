class Node:
    def __init__(self, HeSo, SoMu):
        self.HeSo = HeSo
        self.SoMu = SoMu
        self.KeTiep = None

class DATHUC:
    def __init__(self):
        self.head = None

    def Chep(self):
        new_dathuc = DATHUC()
        current = self.head
        while current:
            new_node = Node(current.HeSo, current.SoMu)
            if new_dathuc.head is None:
                new_dathuc.head = new_node
            else:
                prev_node.KeTiep = new_node
            prev_node = new_node
            current = current.KeTiep
        return new_dathuc

# Ví dụ sử dụng:
dathuc = DATHUC()
dathuc.head = Node(2, 3)
second = Node(5, 2)
third = Node(-3, 1)
dathuc.head.KeTiep = second
second.KeTiep = third

dathuc_copy = dathuc.Chep()
print("Đa thức gốc:")
current = dathuc_copy.head
while current:
    print(f"{current.HeSo}x^{current.SoMu}", end=" ")
    current = current.KeTiep
print()
