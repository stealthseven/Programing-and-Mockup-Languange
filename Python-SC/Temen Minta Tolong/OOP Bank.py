class Bank:
    def __init__(self, noRek, nama, saldo, telp, alamat, email, nik):
        self.noRek = noRek
        self.nama = nama
        self.saldo = saldo
        self.telp = telp
        self.alamat = alamat
        self.email = email
        self.nik = nik

    def tampikanData(self):
        print(self.noRek)
        print(self.nama)
        print(self.saldo)
        print(self.telp)
        print(self.alamat)
        print(self.email)
        print(self.nik)


Ajrin = Bank("nr01", "budi", 2000, 21564548,
             "ndemblaksari", "budi@gmail.com", 19000164916)
tampilkanDataAjrin = Ajrin.tampikanData()

print(tampilkanDataAjrin)
