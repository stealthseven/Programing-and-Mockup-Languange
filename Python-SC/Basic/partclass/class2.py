#class of methode 1
class mahasiswa():
    nama = "nama"
    
    def belajar(self, kondisi):
        print(self.nama, 'sedang belajar', kondisi)

    def tidur(self):
        print(self.nama, 'tidur di kelas')

#main program
fredy = mahasiswa()
stepan = mahasiswa()

fredy.nama = "fredy subejo"
stepan.nama = "stepanol subino"

fredy.belajar('dengan giat')
stepan.tidur()
