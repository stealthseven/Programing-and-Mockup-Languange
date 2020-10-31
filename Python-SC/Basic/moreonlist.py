#more on list 

barang = ["sepeda", "kacamata", "duit", "komputer", "kaos kaki"]
print(barang)

#beberapa method untuk memanipulas/merubah list
#method untuk menambah data dalam list
barang.append("tas ransel")
print(barang)

barang.extend("gelas")
print(barang)

barang.insert(4,"sepeda")
print(barang)

#method menghitung anggota
jumlahSepeda = barang.count("sepeda")
print("jumlah sepeda adalah", jumlahSepeda)

#remove data list 
barang.remove("sepeda")
print(barang)

barang.reverse()
print(barang)


print(75*"=")
barang2 = barang.copy() #menggunakan copy agar membuat list baru untuk "barang2" dan tidak merubah "barang"
barang2.append("buku")
print(barang2)
print(barang)



print(100*"=")
#queues
from collections import deque

antrian = deque([1,2,3,4,5])

print("data sekarang: ", antrian)

#menambahkan data 
antrian.append(6)
print("data masuk: ", 6)
print("data sekarang: ", antrian)

antrian.append(7)
print("data masuk: ", 7)
print("data sekarang: ", antrian)
       
antrian.append(8)
print("data masuk: ", 7)
print("data sekarang: ", antrian)
      
#mengurangi antrian
out = antrian.popleft()
print("data keluar: ", out)
print("data sekarang: ", antrian)



print(100*"=")
#stack
tumpukan = [1,2,3,4,5]
print('data sekarang', tumpukan)

#memasukan data baru 
tumpukan.append(6)
print('data masuk', 6)
print('data sekarang', tumpukan)

tumpukan.append(7)
print('data masuk', 7)
print('data sekarang', tumpukan)

tumpukan.append(8)
print('data masuk', 8)
print('data sekarang', tumpukan)

tumpukan.pop()
print('data sekarang' , tumpukan)

print(75*"=")

#queues
from collections import deque

antrian = deque([1,2,3,4,5])

print("data sekarang: ", antrian)

#menambahkan data 
antrian.append(6)
print("data masuk: ", 6)
print("data sekarang: ", antrian)

antrian.append(7)
print("data masuk: ", 7)
print("data sekarang: ", antrian)
        
antrian.append(8)
print("data masuk: ", 7)
print("data sekarang: ", antrian)
        
#mengurangi antrian
out = antrian.popleft()
print("data keluar: ", out)
print("data sekarang: ", antrian)