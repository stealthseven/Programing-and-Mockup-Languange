#looping "while"

angka = 0                 #menggunakan variabel statement(syarat)
while angka < 5:
    print("nilai angka adalah", angka)
    angka = angka + 1
    
print("diluar while")
print(75*"=")


start = True             #menggunakan variable bolean(true/false)
angka = 0

while start:
    print("didalam while loop ke-",angka)
    if angka is 100:
        start = False
        print("angka 100 terlah di temukan")
    angka += 1
print("diluar while")

print(75*"=")

#while II (else,break,continue,pass)
angka = 0               
while angka < 5:
    print("nilai angka adalah", angka)
    angka = angka + 1
else:
    print("nilai angka di akhir while adalah",angka)

print(75*"=")

#while II (else,break,continue,pass)
angka = 0               
while angka < 14:
   if angka is 5:
       break
   print("nilai angka adalah", angka)    #tidak dijalan kan karena "break" langsung menghentikan progranm dan fungsi while berhenti
   angka = angka + 1
else:
   print("nilai angka di akhir while adalah",angka)

print(75*"=")

#while II (else,break,continue,pass)
#angka = 0               
#while angka < 14:
#    if angka is 5:
#        print("check point 1")
#        continue
#        
#    print("nilai angka adalah", angka)    #stuck karena invinite loop
#   angka = angka + 1                     #tidak ada update
#else:
#    print("nilai angka di akhir while adalah",angka)

print(75*"=")

#while II (else,brak,continue,pass)
angka = 0               
while angka < 14:
    if angka is 5:
        print("check point 1 (nilai angka adalah 5)")
        angka += 1
        continue
    print("nilai angka adalah", angka)    #di angka kelima tidak berjalan karena continue langsung kembali menjalankan program while tanpa melewati tahap ini
    angka += 1
else:
    print("nilai angka di akhir while adalah",angka)

print(75*"=")

#while II (else,brak,continue,pass)
angka = 0               
while angka < 14:
    if angka is 5:
        pass
    print("nilai angka adalah", angka)    #tetap menjalankan program  
    angka += 1
else:
    print("nilai angka di akhir while adalah",angka)