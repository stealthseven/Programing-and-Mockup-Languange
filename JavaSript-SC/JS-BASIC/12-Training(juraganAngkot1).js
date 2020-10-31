var penumpang = [];
var tambahPenumpang = function (namaPenumpang, penumpang) {
    // Jika angkot Kosong 
    if (penumpang.length == 0) {
        // tambah penumpang di awal array
        penumpang.push(namaPenumpang);
        // kembalikan isi array dan keluar fungsi
        return penumpang;
    } else {
        // telusuri seluruh kursi dari awal 
        for (var i = 0; i < penumpang.length; i++) {
            // jika ada kursi kosong 
            if (penumpang[i] == undefined) {
                // tambahkan penumpang di kursi tersebut
                penumpang[i] = namaPenumpang;
                // kembalikan isi array dan keluar fungsi                 
                return penumpang;
                // jika sudah ada nama yang sama
            } else if (penumpang[i] == namaPenumpang) {
                // tampilkan pesan kesalahan
                console.log(namaPenumpang + 'sudah ada penumpang');
                // kembalikan isi array
                return penumpang;
                // jika seluruh kursi terisi 
            } else if (i == penumpang.length - 1) {
                // tambah penumpang di akhir array
                penumpang.push(namaPenumpang);
                // kembalikan isi array dan keluar fungsi
                return penumpang;
            }
        }
    }
}

var coba = tambahPenumpang("budhi")
console.log(coba)