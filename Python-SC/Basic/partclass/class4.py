#class of methode 3
#private attribute

class mahasiswa():

    jurusan = "teknik informatika"
    __nilai = 0 #private

    def __init__(self, inputNama, inputNim):
        self.nama = inputNama  #publik
        self.nim = inputNim    #publik

    def uts(self, inputNilai):
        self.__nilai += inputNilai

    def uas(self, inputNilai):
        self.__nilai += inputNilai

    def checkNilai(self):
        if self.__nilai <= 65 :
            print(self.nama, 'tidak lulus')
        else:
            print(self.nama, 'lulus')

#main program

otong = mahasiswa("otong surotong", 1977001)
budun = mahasiswa("budud bin atang", 1977002)

otong.uts(30)
otong.uas(50)
otong.checkNilai()
budun.uts(10)
budun.uas(20)
budun.checkNilai()