#set/himpunan
#Himpunan tidak tergantung pada urutan dan frekuensi datanya

superhero = { "emak" , 
              "wiro sableng" , 
              "ndableg" , 
              "gundala" 
}

print(superhero)
print(type(superhero))

print(76*"=")

makananKambing = set()

makananKambing.add("rumput")
makananKambing.add("daun")
makananKambing.add("dedak")
makananKambing.add("kolonjono")

print(makananKambing)

ganjil = {1,3,5,7,9}
genap = {2,4,6,8,10}
prima = {2,3,5,7}

print(ganjil.union(genap))        # gabungan
print(ganjil.intersection(prima)) # irisan

