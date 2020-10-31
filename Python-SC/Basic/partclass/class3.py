#class of methode 2
#__init__

class mahasiswa():

    def __init__(self, inputNama, inputNim):
        self.nama = inputNama
        self.nim = inputNim

    def belajar(self, kondisi):
        print(self.nama, 'sedang belajar', kondisi)

    def tidur(self):
        print(self.nama, 'tidur di kelas')

#main program

otong = mahasiswa("otong surotong", 1977001)

print(otong.nama)
print(otong.nim)
otong.nama = "atang binatang"  #dengan adanya ini akan mudah sekali data kita untuk di hack/dirubah seseorang
print(otong.nama)              #seharusnya variable seperti ini terproteksi(di lindungi)

otong.tidur()