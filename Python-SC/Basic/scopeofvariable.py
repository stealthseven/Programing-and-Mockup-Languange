#scope of variable
#scope variable : lokal 

namaKucing = "tongtong"    #variable global                 

def rubahNamaKucing(namaBaru):
    namaKucing = namaBaru                                  #nama kucing di fungsi ini adalah lokal 
    print("saya merubah nama kucing menjadi", namaKucing)    

rubahNamaKucing("bodong")
print("nama kucing saya menjadi", namaKucing)              #nama kucing disini tidak berubah karena variable global

print(100*"=")
#scope of variable
#scope variable : global

namaKucing = "tongtong"    #variable global                 

def rubahNamaKucing(namaBaru): 
    global namaKucing                       #dengan fungsi ini merubah variable global
    namaKucing = namaBaru                                   
    print("saya merubah nama kucing menjadi", namaKucing)    

rubahNamaKucing("bodong")
print("nama kucing saya menjadi", namaKucing)              

print(100*"=")
#scope of variable
#scope variable : global

namaKucing = "tongtong"
makananKucing = "gereh"

def rubahNamaKucing(namaBaru): 
    global namaKucing                       #variable global
    namaKucing = namaBaru                   #variable global
    namatest = namaBaru                     #variable lokal
    print("saya merubah nama kucing menjadi", namaKucing)  
    print(namatest)                         #hanya berjalan pada definisi ini(rubah nama kucing) karena lokal
    
def kasihMakanKucing(makanan,nama):
    global namaKucing,makananKucing          #variable global (bila tidak ter aplikasi oleh "global" maka itu adalah scope lokal)
    namaKucing = nama
    makananKucing = makanan

rubahNamaKucing("bodong")
kasihMakanKucing("tempe","pussii")
print("nama kucing saya menjadi",namaKucing,"dan makan",makananKucing)  
