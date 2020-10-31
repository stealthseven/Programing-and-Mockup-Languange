#class of variable
class mahasiswa():

    jumlah_mahasiswa = 0 

    def __init__(self, inputNama, inputNim):
        self.nama = inputNama
        self.nim = inputNim 
        mahasiswa.jumlah_mahasiswa += 1

#main programs

otong = mahasiswa('otong surotong', 1977001)
bejo = mahasiswa('bejo prayitno', 1977002)
evan = mahasiswa('evan budi buduni', 1977003)

print(mahasiswa.jumlah_mahasiswa)