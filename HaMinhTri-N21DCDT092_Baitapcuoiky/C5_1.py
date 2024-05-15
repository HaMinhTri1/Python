class treenode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def SoNut(self, root):
        if root is None:
            return 0
        return 1 + self.SoNut(root.left) + self.SoNut(root.right)

if __name__ == "__main__":
    # Tạo cây nhị phân
    root = treenode(10)
    root.left = treenode(5)
    root.right = treenode(15)
    root.left.left = treenode(3)
    root.left.right = treenode(7)
    root.right.left = treenode(12)
    root.right.right = treenode(20)

    # Tính số nút của cây
    cay = treenode(10)
    so_nut = cay.SoNut(root)
    print(f"Số nút của cây là: {so_nut}")