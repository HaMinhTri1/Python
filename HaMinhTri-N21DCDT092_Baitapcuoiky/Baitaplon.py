class Muctu:
    def __init__(self, tu = None, nghia = None,loaitu = None, viDu = None):
        self.tu = tu
        self.loaitu = loaitu
        self.nghia = nghia
        self.viDu = viDu
        self.left = None
        self.right = None
    def __str__(self):
        return f"{self.tu}\nnghĩa: {self.nghia}\nloại từ: {self.loaitu}\nVí dụ: {self.viDu}"
class Dictionary:
    def __init__(self):
        self.root = None
    def insert(self, tu, nghia, loaitu, viDu):
        self.root = self.insert_recursive(self.root,tu,nghia,loaitu,viDu)
    def insert_recursive(self, node,tu,nghia,loaitu,viDu):
        if not node:
            return Muctu(tu,nghia,loaitu,viDu)
        if tu <node.tu:
            node.left = self.insert_recursive(node.left,tu,nghia,loaitu,viDu)
        elif tu > node.tu:
            node.right = self.insert_recursive(node.right,tu,nghia,loaitu,viDu)
        return node
    def timtu(self, tu):
        def timturecursive(node, tu):
            if not node or node.tu == tu:
                return node
            if tu < node.tu:
                return timturecursive(node.left, tu)
            else:
                return timturecursive(node.right,tu)
        result = timturecursive(self.root, tu)
        if result is None:
            print(f"Từ '{tu}' không có trong từ điển")
        else:
         print(f"nghĩa: {result.nghia}\nloại từ: {result.loaitu}\nVí dụ: {result.viDu}")
    def insertfile(self,node): 
        def timturecursive(node, tu):
            if not node or node.tu == tu:
                return node
            if tu < node.tu:
                return timturecursive(node.left, tu)
            else:
                return timturecursive(node.right,tu)
        result =  timturecursive(self.root,node)
        node = result
        file = open('N21DCDT092_BST.txt', 'a',encoding='utf8')
        file.write(str(node.tu)+'\n')
        file.write(str(node.nghia)+'\n')
        file.write(str(node.loaitu)+'\n')
        file.write(str(node.viDu) +'\n')
        file.close
    def delete(self, tu):
        self.root = self.delete_recursive(self.root, tu)
    def delete_recursive(self,node,tu):
        if not node:
            return node
        if tu < node.tu:
            node.left = self.delete_recursive(node.left, tu)
        elif tu > node.tu:
            node.right = self.delete_recursive(node.right, tu)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            min_right = self._find_min(node.right)
            node.word, node.meaning = min_right.word, min_right.meaning
            node.right = self._delete_recursive(node.right, min_right.word)
        return node
    def _find_min(self, node):
        while node.left:
            node = node.left
        return node
    def naptutaptin(self,node):
        global tutaptin,nghiataptin,loaitutaptin,viDutaptin
        fhand = open('N21DCDT092_BST.txt',encoding='utf8')
        list_ =  fhand.readlines()
        for i in range(len(list_)):
           list_[i] = list_[i].rstrip("\n")
        value = node
        index = list_.index(value)
        tutaptin = list_[index]
        nghiataptin = list_[index+1]
        loaitutaptin = list_[index+2]
        viDutaptin = list_[index+3]
        Dictionary.insert(self,tutaptin,nghiataptin,loaitutaptin,viDutaptin)
                    
def tao_menu():
    print("\n============== MENU ==============")
    print("1. Thêm một mục từ mới vào từ điển.")
    print("2. Loại bỏ một mục từ của từ điển.")
    print("3. Tra cứu các nghĩa của một mục từ trong từ điển.")
    print("4. Lưu từ điển vào các tập tin.")
    print("5. Nạp từ điển từ các tập tin.")
    print("6. Kết thúc chương trình.")


if __name__ == "__main__":
    tu_dien = Dictionary()
    while True:
        tao_menu()
        lua_chon = input("Nhập lựa chọn của bạn: ")

        if lua_chon == '1':
            tu_moi = input("Nhập từ mới: ")
            nghia_moi = input("Nhập nghĩa cho từ mới: ")
            loaitu_moi = input("Nhập loại từ: ")
            viDu_moi = input("Nhập ví dụ: ")
            tu_dien.insert(tu_moi,nghia_moi,loaitu_moi,viDu_moi)
        elif lua_chon == '2':
            tu_can_xoa = input("Nhập từ cần xóa: ")
            tu_dien.delete(tu_can_xoa)
        elif lua_chon == '3':
            tu_can_tra_cuu = input("Nhập từ cần tra cứu: ")
            tu_dien.timtu(tu_can_tra_cuu)
        elif lua_chon == '4':
            ten_tu = input("Nhập từ để lưu từ điển: ")
            tu_dien.insertfile(ten_tu)
        elif lua_chon == '5':
            tunapvao = input("Nhập tên tập tin để nạp từ điển: ")
            tu_dien.naptutaptin(tunapvao)
        elif lua_chon == '6':
            print("Kết thúc chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")
