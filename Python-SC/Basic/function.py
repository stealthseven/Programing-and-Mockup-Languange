#function

def fungsi():
    print("ini adalah fungsi")
    
fungsi()

print(100*"=")
#membuat fungsi sederhana 1

def jenis_ayam():
    print("ayam kate")
    
def harga_ayam():
    jenis_ayam()
    print("harga dari jenis ayam adalah Rp. 50.000")

harga_ayam()

print(100*"=")
#membuat fungsi dengan argumen

def jenissapi():
    print("sapi limosin")
def hargasapi():
    jenissapi()
    print("harga sapi /ekor adalah 37 juta")
#argumen

def hargadagingsapi(kg):
    jenissapi()
    harga_kilo = 85000
    hargatotal = kg*harga_kilo
    print('harga',kg,'daging sapi adalah', hargatotal )

hargasapi()
hargadagingsapi(5)

print(100*"=")
#fungsi menggunakan argumen sederhana 2

def siswa(nama):
    print("siswa ini bernama", nama)
siswa("mario")

print(100*"+")

#fungsi dengan menggunkan keywords argument
def guru(nama,pelajaran):
    print("guru ini bernama : ",nama)
    print("mengajar pelajaran : ",pelajaran)
    
guru(nama="pak entis",pelajaran="kimia")
guru(pelajaran="Fisika",nama="pak sudir")
guru("bu susan", "biologi")
guru("seni pahat", "pak budi") #contoh salah

print(100*"+")

#fungsi menggunakan default argumen

def penjagasekolah(nama,asal="yogyakarta",shift="siang"):
    print("penjaga sekolah ini bernama :", nama)
    print("penjaga sekolah ini berasal :", asal)
    print("penjaga sekolah ini bekerja pada shift? :", shift)
    
penjagasekolah("darno")
penjagasekolah("sugiono", shift="malam")
penjagasekolah("sugiman", asal="bantul")
#penjagasekolah(shift="malam", asal="kulon progo") [eror karena 1 argumen "nama tidak di inputkan"]

print(100*"=")
#Fungsi dengan return value

def kuadrat(argumen):
    total = argumen**2
    print("nilai kuadrat dari",argumen,"adalah",total)
    return total 
a = kuadrat(4)
print(a)

print(100*"=")
#fungsi dengan return value dan multiplke argumen

def tambah(argumen1,argumen2):
    total = argumen1 + argumen2 
    print(argumen1,'+',argumen2,'=', total)
    return total 
def kali(argumen1,argumen2):
    total = argumen1 * argumen2 
    print(argumen1,'X',argumen2,'=', total)
    return total 

a = tambah(2,9)
b = kali(4,a)
print(b)

print(100*"=")
#anonymous function
#lamda

LuasSegitiga = lambda tinggi,alas: tinggi*alas/2
hasil = LuasSegitiga(8,6)
print("hasil dari luas segitiga adalah",hasil)
