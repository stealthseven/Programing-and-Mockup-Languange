// Direct object
var mahasiswa = {
    nama: "ucup",
    nim: 190023122,
    alamat: "bengkulu",
    ipk: [3.00, 32.00, 31.00, 30.50]
}
// obeject dengan fungsi deklarasi
function mhs(nama, nim, alamat, ipk) {
    var dataMhs = {}
    dataMhs.nama = nama;
    dataMhs.nim = nim;
    dataMhs.alamat = alamat;
    dataMhs.ipk = ipk;
    return dataMhs
}
var mhs1 = mhs("ucup", 10298090, "jogja", [20, 21, 36, 43])

// object dengan constructor
function PesanApa(makanan, minuman) {
    this.makanan = makanan;
    this.minuman = minuman;
}

var paketSatu = new PesanApa("nasi goreng", "es jeruk")

// materi this
// cara 1 - fungsi deklarasi
function sapa() {
    console.log(this);
    console.log("halo");
}
this.sapa();
// mengembalikan object global

// cara 2 - object literal 
var a = {};
a.sapa = function () {
    console.log(this);
    console.log('haloha')
}
a.sapa();
// this mengembalikan object yang bersangkutan 

// cara 3 - constructor
function halo() {
    console.log(this);
    console.log('haloha');
}
var aku = new halo();
var aku2 = new halo();
// this mengembalikan obeject yang baru di buat