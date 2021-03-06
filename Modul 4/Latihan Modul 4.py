##if target in arrayTempatYangDicari:
##    print("tergetnya terdapat di array itu")
##else :
##    print("targetnya tidak terdapat di array itu")

##A = [10,51,2,18,4,31,13,5,23,64,29]
################################################################################

def cariLurus(wadah, target):
    n = len(wadah)
    for i in range(n):
        if wadah[i] == target:
            return True
        return False

################################################################################
    
##import modul Mahasiswa
import Mahasiswa as ms
        
c0 = ms.MhsTIF('Ika',10,'Sukoharjo',240000)
c1 = ms.MhsTIF('Budi',51,'Sragen',230000)
c2 = ms.MhsTIF('Ahmad',2,'Surakarta',250000)
c3 = ms.MhsTIF('Chandra',18,'Surakarta',235000)
c4 = ms.MhsTIF('Eka',4,'Boyolali',240000)
c5 = ms.MhsTIF('Fandi',31,'Salatiga',240000)
c6 = ms.MhsTIF('Deni',13,'Klaten',245000)
c7 = ms.MhsTIF('Galuh',5,'Wonogiri',245000)
c8 = ms.MhsTIF('Janto',23,'Klaten',245000)
c9 = ms.MhsTIF('Hasan',64,'Karanganyar',270000)
c10 = ms.MhsTIF('Khalid',29,'Purwodadi',265000)
##
##Lalu kita membuat daftar mahasiswa dalam bentuk list seperti ini:
##
Daftar = [c0,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10]

target = 'Klaten'
for i in Daftar :
    if i.kotaTinggal == target:
        print(i.nama + ' tinggal di ' + target)

##def cari(n):
##    baru = []
##    for i in range(len(n)):
##        if(n[i].asal.lower() == 'klaten'):
##            baru.append(i)
##    return baru
##print(cari(daftar))

################################################################################
        
def cariTerkecil(kumpulan):
    n = len(kumpulan)
    #Anggap item pertama adalah yang terkecil
    terkecil = kumpulan[0]
    #tentukan apakah item lain lebih kecil
    for i in range(1,n):
        if kumpulan[i] < terkecil:
            terkecil = terkecil[i]

    return terkecil  #kembalikan yang terkecil

##Bagaimana programnya jika kita ingin mencari mahasiswa
##(dari class MhsTIF di atas) yang uang sakunya terkecil?
def kecil(Daftar):
    minim = Daftar[0].uangSaku
    for i in Daftar:
        if i.uangSaku < minim:
            minim = i.uangSaku
            if i.uangSaku == minim:
                nama = i.nama
    return nama, minim
print(kecil(Daftar))

##Bagaimana kalau yang terbesar?
def besar(Daftar):
    maxim = Daftar[0].uangSaku
    for i in Daftar:
        if i.uangSaku > maxim:
            maxim = i.uangSaku
            if i.uangSaku == maxim:
                nama = i.nama
    return nama, maxim
print(besar(Daftar))

##Bagaimanakah programnya jika kita ingin mencari semua mahasiswa
##yang uang sakunya kurang dari 250ribu?
def kurang(Daftar):
    a=[]
    for i in Daftar:
        if i.uangSaku < 250000:
            a.append(i.nama)
    return a
print(kurang(Daftar))

##Bagaimana kalau lebih?
def lebih(Daftar):
    a = []
    for i in Daftar:
        if i.uangSaku >= 250000:
            a.append(i.nama)
    return a
print(lebih(Daftar))

################################################################################

def binSe(list, terget):
    #mulai dari seluruh runtutan elemen
    low = 0
    high = len(list) - 1

    #secara berulang belah runtutan itu menjadi separuhnya
    #   sampai targetnya ditemukan
    while low <= high:
            #temukan pertengahan runtut itu
        mid = (high + low) // 2
            #Apakah pertengahanya semua target?
        if list[mid] == target:
            return True
            #ataukah targetnya di sebelah kirinya?
        elif target < list[mid]:
            high = mid - 1
            #atau targetnya ada di sebelah kananya?
        else:
            low = mid + 1
        #jika runtutnya tidak bisa dibelah lagi, berarti targetnya tidak ada
    return False
list = [2,3,5,6,6,6,8,9,9,10,11,12,13,13,14]
target = 6
print(binSe(list,target))
list = [2,3,5,6,6,6,8,9,9,10,11,12,13,13,14]
target = 7
print(binSe(list,target))

##Dapatkah kamu mengubah programnya agar dia mengembalikan index-nya kalau
##targetnya ditemukan,dan mengembalikan False kalau target tidak ditemukan?

def binSe(list, target):
    a=[]
    low = 0
    high = len(list) - 1
    while(low<=high):
        mid = (low+high)//2
        if(list[mid] == target):
            a.append(list.index(target))
            i=list.index(target)-1
            j = list.index(target) + 1
            while target == list[i]:
                a.append(i)
                i-=1
            while target == list[j]:
                a.append(j)
                j+=1
            return a
        elif(target<list[mid]):
            high = mid - 1
        else:
            low = mid + 1
    return False

list = [2,3,3,3,4,4,4,4,4,5,6,6,8,9,9,10,11,12,13,13,14]
target = 6
print(binSe(list,target))
list = [2,3,5,6,6,6,8,9,9,10,11,12,13,13,14]
target = 7
print(binSe(list,target))

