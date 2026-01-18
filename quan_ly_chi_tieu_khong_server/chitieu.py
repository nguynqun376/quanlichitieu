class ChiTieu:
    def __init__(self, ten, so_tien, ngay):
        self.ten = ten
        self.so_tien = so_tien
        self.ngay = ngay


class QuanLyChiTieu:
    def __init__(self):
        self._ds = []

    def them(self, ten, so_tien, ngay):
        self._ds.append(ChiTieu(ten, so_tien, ngay))

    def danh_sach(self):
        return self._ds
