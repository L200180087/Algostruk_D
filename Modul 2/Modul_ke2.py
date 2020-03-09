#No 1
class Pesan(object) :
    """
        Sebuah class bernama Pesan.
        Untuk memahami konsep Class dan Object
    """
    def __init__(self, sebuahString) :
        self.teks = sebuahString
        
    def cetakIni(self) :
        print(self.teks)
        
    def cetakPkaiHurufKapital(self):
        print(str.upper(self.teks))
        
    def cetakPakaiHurufKecil(self) :
        print(str.lower(self.teks))
        
    def jumKar(self) :
        return len(self.teks)
    
    def cetakJumlahKarakterku(self) :
        print("Kalimatku mempunyai", len(self.teks), "karakter.")
        
    def perbarui(self,stringBaru):
        self.tekt = stringBaru
        
    #(a)      
    def apakahTerkandung(self, kandung) :
        if kandung in self.teks :
            print(True)
        else :
            print(False)
            
    #(b)        
    def hitungKonsonan(self) :
        vokal = "AIUEOaiueo"
        numvoc = 0
        teks_len = len(self.teks)
        for i in self.teks :
            if i in vokal :
                numvoc = numvoc + 1
        return teks_len - numvoc
    
    #(c)
    def hitungVokal(self) :
        vokal = "AIUEOaiueo"
        numvoc = 0
        teks_len = len(self.teks)
        for i in self.teks :
            if i in vokal :
                numvoc = numvoc + 1
        return numvoc
                
        
class sembarangKelas(object) :
    def metodeSatu(self):
        pass
    def metodeSembilan(self, stringBaru) :
        pass

#No 2  
class Manusia(object) :
    keadaan = "Lapar"
    def __init__(self, nama) :
        self.nama = nama
        
    def ucapkanSalam(self) :
        print("Salam, namaku", self.nama)
        
    def makan(self, s):
        print("Saya baru aja makan", a)
        self.keadaan = "Kenyang"
        
    def olahraga(self, k) :
        print("Saya baru saja latihan", k)
        self.keadaan = "Lapar"

class Mahasiswa(Manusia) :
    def __init__(self,nama,NIM,kota,us) :
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us
        
    def __str__(self) :
        s = self.nama + ", NIM "+ str(self.NIM) + ", Tinggal di " + self.kotaTinggal + ", Uang saku Rp "+ str(self.uangSaku)+" tiap bulannya."
        return s

    def ambilNama(self):
        return self.nama
    
    def ambilNIM(self):
        return self.NIM
    
    #(a)
    def ambilKotaTinggal(self) :
        return self.kotaTinggal

    #(b)
    def perbaruiKotaTinggal(self, kotaBaru) :
        self.kotaTinggal = kotaBaru

    #(c)
    def ambilUangSaku(self):
        return int(self.uangSaku)

    def tambahUangSaku(self, tambahUS) :
        self.uangSaku = int(self.uangSaku)+tambahUS

    def makan(self,s):
        print("Saya baru saja makan",s,"sambil belajar.")
        self.keadaan = "Kenyang"
#No 4
    listKuliah=[]
    def ambilKuliah(self, makul) :
        self.listKuliah.append(makul)
        
#No 5
    def hapusKuliah(self, makul) :
        self.listKuliah.remove(makul)
        
#No 6        
class SiswaSMA(Manusia):
    def __init__(self, nama, NISN, uangSaku, alamat):
        self.nama = nama
        self.nisn = NISN
        self.uangSaku = uangSaku
        self.alamat = alamat
        
    def __str__(self):
        return 'Nama      : ' + str(self.nama) + "\n" + 'NISN      : ' + str(self.nisn) + "\n" +'Alamat    : ' + str(self.alamat) + "\n" +'Uang Saku : ' + str(self.uangSaku)

    
    def ambilNama(self):
        return self.nama
    
    def ambilNisn(self):
        return self.nisn
    
    def ambilUangSaku(self):
        return self.uangSaku

    def ambilKotaTinggal(self):
        return self.kotaTinggal

    def perbaruiKotaTinggal(self,stringbaru):
        self.kotaTinggal = stringbaru

    def tambahUangSaku(self,tambah):
        self.uangSaku += tambah
        
#No 7
#
#Metode dan  state yang tampak di object itu berasal dari semua class, dari Manusia, Mahasiswa, atau MhsTIF.
#Ini adalah konsep pewarisan. MhsTIF mewarisi sifat Manusia dan Mahasiswa
#Karena MhsTIF adalah anak kelas dari Mahasiswa dan Mahasiswa adalah anak kelas Manusia
#

#No 3
a = input("Masukkan Nama      : ")
b = input("Masukkan NIM       : ")
c = input("Masukkan Kota      : ")
d = input("Masukkan Uang Saku : ")

m1 = Mahasiswa(a,b,c,d)
print(m1)
