class Mahasiswa():
    def __init__(self, nama, nim, kota, us):
        self.nama = nama
        self.NIM = nim
        self.kotaTinggal = kota
        self.uangSaku = us
class MhsTIF(Mahasiswa):
    def katakanPy(self):
        print("Hallo")
