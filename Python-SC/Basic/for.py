#perulangan "for"
#list sebagai iterable
gorengan = ["bakwan","tempe goreng", "tahu goreng", "ubi goreng", "cakar goreng tepung", "gembus"]

for g in gorengan:
    print(g)
    print(len(g))
    
print(75*"=")

#string sebagai iterable
tempe = "tempe"
for i in tempe:
    print(i)
    
print(75*"=")

#for di dalam for

lauk = ["ikan","ayam","begedel","sosis goreng","tempe","tahu"]
sayur = ["kangkung","kelor","rebung","pare","sop"]
minuman = ["es jeruk","es teh","lemontea","milkshake","susu","kopi"]

daftar_menu = [lauk,sayur,minuman]
for RMmenyediakan in daftar_menu:
    print(RMmenyediakan)
    for macam2 in RMmenyediakan:
        print(macam2)

print(75*"=")

#perulangan "for" II
nomor = 27
for i in range(0,35):
    print(i)
    if i is nomor:
        print("angka ditemukan", nomor)
        break                            #untuk memberhentikan perulangan bila angka telah ditemukan
else:
    print("angka tidak ditemukan")
    
print("program di luar for")             #Di luar loop "for"

print(75*"=")

#perulangan "for" II
nomor = 42
for i in range(0,70,2):
    print(i)
    if i is nomor:
        print("angka ditemukan", nomor)
        break                            #untuk memberhentikan perulangan bila angka telah ditemukan
else:
    print("angka tidak ditemukan")

print(75*"=")

#perulangan "for" II
nomor = 120
for i in range(0,70,5):
    print(i)
    if i is nomor:
        print("angka ditemukan", nomor)
        break                            #untuk memberhentikan perulangan bila angka telah ditemukan
else:
    print("angka tidak ditemukan")

print(75*"=")

#continue & pass 1
#for III
for i in range(1,20):
    if i is 8:
        print("nilai i adalah 8")
        break
    print("nilai saat ini adalah", i)
else:
    print("akhir dari loop")    #tidak terbaca "break" langsung mengakhiri program
print("diluar loop")

print(75*"=")

#continue & pass 2
#for III
for i in range(1,20):
    if i is 8:
        print("nilai i adalah 8")
        continue                   #fungsi melanjutkan ke step berikutnya
        print("cek 1")             #tidak berjalan karena continue langsung ke melanjutkan fungsi
    print("nilai saat ini adalah", i)
else:
    print("akhir dari loop")    
print("diluar loop")

print(75*"=")

#continue & pass 2
#for III
for i in range(1,20):
    if i is 8:
        print("nilai i adalah 8")
        pass                       #tidak ada fungsinya[kata kunci kosong agar bisa mengkontruksi fungsi yang dimiliki]
        print("cek 1")             #agar fungsi ini bekerja
    print("nilai saat ini adalah", i)
else:
    print("akhir dari loop")    
print("diluar loop")