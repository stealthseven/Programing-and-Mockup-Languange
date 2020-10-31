#if,else,elif

nilai1 = 75
nilai2 = 44


if nilai1 == 75 : 
    print("nilai anda", nilai1)

    #tidak muncul karena statement salah
    if nilai2 == 80 :                
        print("nilai anda", nilai2)
              
print(75*"=")

angka = 85
if 80 <= angka <= 100 :
    print("nilai anda bagus banget")
elif 70 <= angka <= 80 :
    print("nilai anda bagus")
else :
    print("melakukan perbaikan")

#untuk menunjukan kondisi dapat menggunakan is, nor, is npt DLL
A = 10 
B = 24 
C = 5

if A is 10 :
    print("Angka yang anda masukan benar", A)
if B is not 30 :
    print ("Angka yang dimasukan benar", B)
if not C is 10 :
    print("Angka yang dimasukan salah", C)

#oprator logika untuk list dan string dengan "if"

TokoSembako = ["beras","sarden","ikan","krupuk","saos","kecap"]
beli = ("udang")

if beli in TokoSembako :
    print("ibu2 penjual bilang, ya saya jual", beli)
if not beli in TokoSembako :
    print("ibu2 penjual bilang, ga jual e dek", beli)