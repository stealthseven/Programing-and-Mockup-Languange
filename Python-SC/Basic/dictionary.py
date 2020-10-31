#dictionary
# Mahasiswa1 = "keys" : "value"

Mahasiswa1 = {"Nim":1900,
              "Nama":"susan",
              "status mahasiwa":"aktif"}
              
Mahasiswa2 = {"Nim":1901,
              "Nama":"stiven",
              "status mahasiwa":"cuti"}

listMahasiswa = {1900:Mahasiswa1,1901:Mahasiswa2}

print(listMahasiswa[1900])
print(Mahasiswa1["Nama"])
print(Mahasiswa1.keys())
print(Mahasiswa1.values())
print(Mahasiswa1.items())

