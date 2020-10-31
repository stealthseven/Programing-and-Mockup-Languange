#inharitance
class Ojek():
    def __init__(self, nama, transmisi, daerahkerja):
        self.nama = nama 
        self.transmisi = transmisi
        self.daerahkerja = daerahkerja

    def cek_id(self):
        print('nama',self.nama,'\nmotor :',self.transmisi,'\ndaerah kerja :',self.daerahkerja)

class Grab(Ojek):                        #inheritance (turunan fungsi)

    def cek_id(self):                    #overwrite "cek_id" di class ojek
        print('ojek online, Grab wae')


ojek1 = Ojek('paijo subejo', 'manual','bandung selatan')
ojek2 = Grab('untung bin atang', 'matic', 'jogja selatan')

ojek1.cek_id()
ojek2.cek_id()