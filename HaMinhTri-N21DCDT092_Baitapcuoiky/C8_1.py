class TuDien:
    def __init__(self):
        # Khởi tạo từ điển rỗng
        self.tu_dien = {}

    def NhapTu(self, tu, dong_nghia=None, trai_nghia=None):
        """
        Phương thức để nhập từ và các thông tin liên quan vào từ điển.

        Args:
            tu (str): Từ cần thêm vào từ điển.
            dong_nghia (str, optional): Từ đồng nghĩa của từ. Mặc định là None.
            trai_nghia (str, optional): Từ trái nghĩa của từ. Mặc định là None.
        """
        # Hàm băm: lấy ký tự đầu tiên của từ
        ky_tu_dau = tu[0]

        # Thêm từ và thông tin liên quan vào từ điển
        self.tu_dien[tu] = {'dong_nghia': dong_nghia, 'trai_nghia': trai_nghia, 'ky_tu_dau': ky_tu_dau}

    def TraTu(self, tu):
        """
        Phương thức để tra từ trong từ điển.

        Args:
            tu (str): Từ cần tra cứu.

        Returns:
            dict: Thông tin về từ đồng nghĩa và từ trái nghĩa (nếu có).
        """
        if tu in self.tu_dien:
            return self.tu_dien[tu]
        else:
            return {'dong_nghia': None, 'trai_nghia': None, 'ky_tu_dau': None}

# Sử dụng lớp TuDien
td = TuDien()
td.NhapTu('học', 'học tập', 'lười biếng')
td.NhapTu('thành công', 'thành tựu', 'thất bại')

# Tra từ 'học'
ket_qua_tra_tu = td.TraTu('học')
print(f"Từ đồng nghĩa: {ket_qua_tra_tu['dong_nghia']}")
print(f"Từ trái nghĩa: {ket_qua_tra_tu['trai_nghia']}")
